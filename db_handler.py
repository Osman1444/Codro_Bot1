from supabase import create_client, Client
import os
import json
from datetime import datetime
import httpx
import logging
from typing import Optional, List, Dict, Any

class DatabaseHandler:
    def __init__(self, supabase_url: str, supabase_key: str):
        """Initialize Supabase client with custom timeout settings"""
        try:
            # إنشاء عميل Supabase مع إعدادات مخصصة
            self.supabase: Client = create_client(
                supabase_url,
                supabase_key,
                # لا نحتاج لتمرير خيارات إضافية هنا
            )
            logging.info("✅ تم الاتصال بنجاح بقاعدة البيانات Supabase")
        except Exception as e:
            logging.error(f"❌ خطأ في الاتصال بقاعدة البيانات Supabase: {str(e)}")
            self.supabase = None

    async def save_message(self, user_id: int, message_type: str, message_content: str, 
                         course: Optional[str] = None, score: Optional[int] = None, 
                         total: Optional[int] = None) -> Optional[Dict[str, Any]]:
        """حفظ رسالة في قاعدة البيانات
        
        Args:
            user_id: معرف المستخدم
            message_type: نوع الرسالة (quiz_evaluation, command_response)
            message_content: محتوى الرسالة
            course: اسم الكورس (اختياري)
            score: النتيجة (اختياري)
            total: العدد الكلي للأسئلة (اختياري)
            
        Returns:
            Dict containing the saved data or None if there was an error
        """
        if not self.supabase:
            logging.error("❌ لم يتم الاتصال بقاعدة البيانات")
            return None
            
        try:
            data = {
                'user_id': user_id,
                'message_type': message_type,
                'message_content': message_content,
                'timestamp': datetime.now().isoformat(),
                'course': course,
                'score': score,
                'total': total
            }
            
            # حذف القيم الفارغة
            data = {k: v for k, v in data.items() if v is not None}
            
            # استخدام insert مع timeout مخصص
            response = await self.supabase.table('messages')\
                .insert(data)\
                .execute()
            
            logging.info(f"✅ تم حفظ الرسالة بنجاح لـ user_id={user_id}")
            return response.data
        except Exception as e:
            logging.error(f"❌ خطأ في حفظ الرسالة لـ user_id={user_id}: {str(e)}")
            return None

    async def get_user_messages(self, user_id: int, message_type: Optional[str] = None, 
                              limit: int = 10) -> List[Dict[str, Any]]:
        """استرجاع رسائل المستخدم من قاعدة البيانات
        
        Args:
            user_id: معرف المستخدم
            message_type: نوع الرسالة (اختياري)
            limit: عدد الرسائل المطلوبة
            
        Returns:
            List of messages or empty list if there was an error
        """
        if not self.supabase:
            logging.error("❌ لم يتم الاتصال بقاعدة البيانات")
            return []
            
        try:
            # بناء الاستعلام
            query = self.supabase.table('messages')\
                .select('*')\
                .eq('user_id', user_id)
            
            if message_type:
                query = query.eq('message_type', message_type)
            
            # تنفيذ الاستعلام مع الترتيب والحد
            response = await query\
                .order('timestamp', desc=True)\
                .limit(limit)\
                .execute()
            
            logging.info(f"✅ تم استرجاع {len(response.data)} رسالة لـ user_id={user_id}")
            return response.data
        except Exception as e:
            logging.error(f"❌ خطأ في استرجاع الرسائل لـ user_id={user_id}: {str(e)}")
            return []
