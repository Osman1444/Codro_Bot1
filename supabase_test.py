from supabase import create_client
# from dotenv import load_dotenv
import os
import time

class SupabaseManager:
    def __init__(self):
        self.supabase = create_client(
            'https://rxleurucnmlvswfwvaqo.supabase.co',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4bGV1cnVjbm1sdnN3Znd2YXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY0NTM2MTEsImV4cCI6MjA1MjAyOTYxMX0.1Qb-PurZ2Zyyx1sa2We748xJ9z1U1MDjP4U0J09rfoY'
        )
   
    def save_chat_history(self, telegram_id: int, chat_history: list) -> bool:
        """حفظ أو تحديث سجل المحادثة"""
        try:
            # التحقق إذا كان المستخدم موجود
            existing_chat = self.supabase.table('chat_history')\
                .select("*")\
                .eq('telegram_id', telegram_id)\
                .execute()
            
            data = {
                "telegram_id": telegram_id,
                "chat_history": chat_history
            }
            
            if existing_chat.data:
                # تحديث السجل الموجود
                result = self.supabase.table('chat_history')\
                    .update(data)\
                    .eq('telegram_id', telegram_id)\
                    .execute()
            else:
                # إنشاء سجل جديد
                result = self.supabase.table('chat_history')\
                    .insert(data)\
                    .execute()
            return True
            
        except Exception as e:
            print(f"❌ خطأ في حفظ سجل المحادثة: {str(e)}")
            return False
    
    def get_chat_history(self, telegram_id: int) -> list:
        """استرجاع سجل المحادثة"""
        try:
            result = self.supabase.table('chat_history')\
                .select("chat_history")\
                .eq('telegram_id', telegram_id)\
                .execute()
            
            if result.data:
                return result.data[0]['chat_history']
            return []
            
        except Exception as e:
            print(f"❌ خطأ في استرجاع سجل المحادثة: {str(e)}")
            return []

if __name__ == "__main__":
    # إنشاء instance من الكلاس
    db = SupabaseManager()
    
    # اختبار حفظ واسترجاع المحادثة
    test_chat = [
        {"role": "user", "parts": ["مرحبا"]},
        {"role": "model", "parts": ["أهلاً وسهلاً!"]}
    ]
    
    print("\n🔄 اختبار حفظ المحادثة...")
    db.save_chat_history(123456, test_chat)
    
    print("\n🔄 اختبار استرجاع المحادثة...")
    saved_chat = db.get_chat_history(123456)
    print(f"المحادثة المسترجعة: {saved_chat}")
