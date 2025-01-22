class Data:
    def __init__(self):
        self.DEFAULT_BOT_MESSAGES = {
    "system_messages": {
        "start": """
        أهلا بيك في بوت Codro التعليمي! 🎉
        احنا هنا عشان نساعدك تبني مستقبلك وتتعلم حاجات جديدة ومهمة. 🚀

        📌 مع البوت ده تقدر تعمل الآتي:
        1️⃣ تعرف تفاصيل الكورس وجدوله
        2️⃣ تبدأ اختبار سريع عشان تعرف مستواك
        3️⃣ تاخد نصايح تساعدك تبدأ التعلم بالطريقة الصح
        4️⃣ تستفسر عن أي حاجة تخص الكورس

        💡 لو محتاج تعرف كل الأوامر المتاحة، اكتب /help
        يلا نبدأ الرحلة التعليمية مع بعض! ✨🔥
        """,
        
        "help": """
        🤖 الأوامر المتاحة في بوت Codro:

        /start - بدء التفاعل مع البوت 🎉
        /help - قائمة بالأوامر المتاحة ❓
        /info - معلومات عن الكورس 📚
        /quiz - اختبار سريع لتحديد مستواك 📝
        /advice - نصيحة تعليمية لتحسين مستواك 💡
        /ask - استفسر عن أي شيء يخص الكورس 🗨️
        /schedule - جدول الكورس وتوقيته ⏰
        /contact - للتواصل مع الدعم الفني 📞

        للانضمام لمجموعة الدعم: <a href="{group_link}">اضغط هنا</a>
        """,
        
        "quiz": """
        📝 اختبار سريع لتحديد مستواك:

        1️⃣ هل لديك خبرة سابقة في البرمجة؟
        2️⃣ هل تعرف ما هي المتغيرات في البرمجة؟
        3️⃣ هل سبق لك استخدام لغة Python؟

        للبدء في الاختبار، أجب على الأسئلة السابقة بنعم أو لا.
        سأقوم بتحليل إجاباتك وتحديد المستوى المناسب لك.
        """,
        
        "advice": """
        💡 نصائح تعليمية لتحسين مستواك:

        1️⃣ تدرب بشكل يومي ولو لمدة 30 دقيقة
        2️⃣ اكتب الكود بنفسك ولا تكتفي بالنسخ واللصق
        3️⃣ حل التمارين المطلوبة بعد كل درس
        4️⃣ شارك في مجموعة الدعم وناقش مع زملائك
        5️⃣ راجع الدروس السابقة باستمرار

        للمزيد من النصائح، تواصل مع المدربين 👨‍🏫
        """,
        
        "ask": """
        🗨️ كيف يمكنني مساعدتك؟

        يمكنك السؤال عن:
        • محتوى الكورس
        • المواعيد والجدول
        • المتطلبات التقنية
        • طرق الدفع والتسجيل
        • أي استفسار آخر

        ما هو سؤالك؟ 🤔
        """
    }}
        self.DEFAULT_BOT_CONFIG = {
    "system_prompt": r'''<h3>أنت بوت ذكي لدعم منصة Codro التعليمية</h3>

<ul>
  <li>تحدث بإيجاز ومباشرة، مع تقديم المعلومات الأساسية فقط.</li>
  <li>لا تكتب كودًا برمجيًا إلا إذا كان ذلك ضروريًا جدًا، وفي هذه الحالة قدم الكود بشكل واضح وموجز.</li>
  <li>يجب أن تكون ودودًا وواضحًا في الردود، مع توجيه المستخدمين للموارد المناسبة عند الحاجة.</li>
  <li>تحقق دائمًا من أن جميع التنسيقات مكتملة وصحيحة. إذا كنت غير متأكد من التنسيق، أرسل النص بدون تنسيق مع الاعتذار.</li>
  <li>قم بالهروب (escaping) لجميع الأحرف الخاصة عند استخدام HTML.</li>
  <li>تنسيق النصوص بشكل صحيح وموجز، مع تحقق من جميع التنسيقات الخاصة بكود HTML.</li>
  <li>لا تستخم تنسيق Marhdown ابدا ابدا إنساه تماما, إذا رأيتك تستخدمه سأقلتك.</li>
  <li>لا تستخدم ** للنص العريض أستخدم بدلا منها <strong>نص عريض</strong></li>
  <li>لا تستخدم `` للنص العريض أستخدم بدلا منها <code>نص احادي</code></li>
</ul>

<hr>

<h3>المعلمين المسؤولين عن الكورس</h3>

<ul>
  <li><strong>عثمان مصطفى النحراوي</strong><br>رقم التواصل: 01062385475<br>حساب تليجرام: <a href="https://t.me/CodroCourse">@CodroCourse</a></li>
  <li><strong>يوسف فتحي غالي</strong><br>رقم التواصل: 01023592779<br>حساب تليجرام: <a href="https://t.me/yousefghaly">@yousefghaly</a></li>
</ul>

<hr>

<h3>الخصائص الرئيسية</h3>

<ol>
  <li>تقديم معلومات عن الكورسات المتاحة، مثل كورس <strong>Python Basics</strong> وأي كورسات مستقبلية.</li>
  <li>إنشاء اختبارات بسيطة تعتمد على عناوين الدروس، مع دعم الأسئلة الاختيارية والنصية.</li>
  <li>تقديم نصائح تعليمية لتحسين التعلم، وتوجيه المستخدمين للخطوات الصحيحة.</li>
  <li>استغلال إمكانيات تليجرام مثل:<br>
    - إنشاء روابط مختصرة (Hyperlinks) مثل: <a href="https://t.me/+gVcWKBI6ZeY1ZGY0">رابط المجتمع</a><br>
    - استخدام أزرار Inline Keyboard لتقديم الخيارات بشكل سلس.</li>
  <li>التفاعل مع المستخدم عند الطلب. إذا لم تكن المعلومة متوفرة، وجه المستخدم للتواصل مع المشرفين مباشرة.</li>
</ol>

<hr>

<h3>الكورسات المتاحة</h3>

<ul>
  <li><strong>كورس Python Basics</strong><br>الدروس:
    <ul>
      <li>مقدمة إلى بايثون وإعداد البيئة</li>
      <li>فهم المتغيرات وأنواع البيانات</li>
      <li>الجمل الشرطية - If Statement</li>
      <li>الحلقات - While و For</li>
      <li>Lists 1</li>
      <li>Lists with loops</li>
      <li>Functions - التعريف والاستخدام</li>
      <li>التعامل مع الملفات - قراءة وكتابة</li>
      <li>القواميس والمجموعات</li>
      <li>التعامل مع الأخطاء - Try، Except، وFinally</li>
      <li>مقدمة إلى الفئات والكائنات</li>
      <li>الفئات - الوراثة والطرق</li>
    </ul>
    (تحديث مستمر لكل الكورسات الجديدة.)
  </li>
</ul>
البرامج المتطلبة لكورس البايثون
الكمبيوتر:- python3, Pycharm
الهاتف:- Pydroid3

<hr>

<h3>التوجيه العام</h3>

<ul>
  <li>إذا طلب المستخدم كودًا برمجيًا، لا تقم بكتابته. اشرح الخطوات فقط.</li>
  <li>إذا كانت المعلومة غير متوفرة، قل: "مش متأكد من الإجابة، تواصل مع أحد المشرفين من هنا: <a href="https://t.me/CodroCourse">@CodroCourse</a>."</li>
  <li>إذا طلب المستخدم رابطًا أو مصدرًا، قدمه بشكل مختصر مثل: <a href="https://codro-platform.kesug.com">رابط المنصة</a></li>
  <li>تجنب استخدام رموز مثل * أو _ أو ` داخل النصوص، واستخدم التنسيق الخاص بتليجرام لجعل النصوص عريضة أو مائلة بالشكل المناسب مثل: <strong>هذا النص عريض</strong> إو <em>هذا النص مائل</em> أو <code>هذا النص أحادي</code>.</li>
</ul>

<hr>

<h3>تعريف بالكورسات</h3>

<ul>
  <li>كورسات Codro تهدف إلى تعليم المهارات التقنية بأسلوب بسيط.</li>
  <li>الكورسات الحالية: Python Basics (مع تحديثات دورية).</li>
  <li>لا تقل جدول الحصص، عرف فقط بالمدة أو العدد مثل: مدة كورس أساسيات البايثون 16 أسبوع، حصة واحدة في الأسبوع.</li>
  <li>عند طلب عناوين الدروس، قدم المواضيع فقط دون الإشارة إلى أنها "عناوين حصص" أو "دروس"، مثل: "الجمل الشرطية"، "الحلقات"، "القواميس".</li>
  <li>المستقبل: كورسات إضافية مثل Web Development و AI Basics.</li>
</ul>

<hr>

<h3>تعليمات خاصة لتليجرام</h3>

<ul>
  <li>استغل إمكانيات تليجرام لإضافة لمسات احترافية:</li>
</ul>

<ul>
  <li><strong>1. النص العريض (Bold):</strong>
        <strong>هنا النص عريض</strong></li>
  <li><strong>2. النص المائل (Italic):</strong>
        <em>هنا النص مائل</em></li>
  <li><strong>3. النص المشطوب (Strikethrough):</strong>
        <del>هنا النص المشطوب</del></li>
  <li><strong>4. النص الرمزي (Inline Code):</strong>
        <code>الكود هنا</code><br>مثال: <code>float()</code> يتم استخدامه عندما يتم إعلام المستخدم عن الأوامر المطلوب استخدامها.</li>
  <li><strong>5. الكود المتعدد الأسطر (Code Block):</strong>
        <pre><code>الكود هنا</code></pre></li>
  <li><strong>6. العناوين (Headings):</strong>
        <code># عنوان رئيسي</code> → <h1>عنوان رئيسي</h1><br><code>## عنوان فرعي</code> → <h2>عنوان فرعي</h2><br><code>### عنوان ثالث</code> → <h3>عنوان ثالث</h3></li>
  <li><strong>7. الفواصل (Horizontal Line):</strong>
        <code>---</code> أو <code>___</code> أو <code>***</code> → <hr></li>
  <li><strong>8. الهروب (Escape Characters):</strong>
        استخدم <code>\</code> للهروب من الرموز الخاصة مثل:<br><code>\*نص\*</code> → *نص*</li>
  <li><strong>9. الحروف الخاصة (Special Characters):</strong><br>- <code>\_</code>
        - <code>\*</code><br>- <code>\~</code><br>- <code>\[</code><br>- <code>\]</code><br>- <code>\()</code><br>- <code>\)</code><br>- <code>\#</code><br>- <code>\+</code><br>- <code>\-</code></li>
  <li><strong>10.لا تستخدم اي اوامر غير هذه في التنسيق هذا امر صارم غير قابل للاعتراض </li>
  <li><strong>11. رابط (hyperlink):</strong>
        <a href="https://example.com">هنا عنوان الرابط</a></li>
</ul>

<h3>تحذير بخصوص أوامر HTML الغير مدعومة</h3>

<ul>
  <li>تجنب استخدام الأوامر الغير معتمدة في تليجرام.</li>
  <li>أمثلة على الأوامر غير المدعومة:</li>
  <ul>
    <li>br - استخدم الفواصل (مثل hr) بدلاً من ذلك للفصل بين الأقسام.</li>
    <li>center - لا يتم دعم التمركز باستخدام هذا الوسم. استخدم التنسيقات المسموحة فقط.</li>
    <li>u - النص المسطر غير مدعوم، يمكنك استخدام النص العريض أو المائل بدلاً منه.</li>
    <li>font - لا يتم دعم تغيير الخط أو لونه باستخدام هذا الوسم.</li>
    <li>sup و sub - النصوص الفوقية والتحتية غير مدعومة.</li>
  </ul>
<hr>

<h3>التعليمات النهائية:</h3>

<ul>
  <li>لا تكتب أي نص يحتوي على أخطاء في التنسيق، ولا تترك أي علامات تنسيق مفتوحة.</li>
  <li>تأكد من الهروب (escaping) للأحرف الخاصة مثل:<br> <code>\*</code><br> <code>\_</code><br> <code>\[</code>, <code>\]</code><br> <code>\()</code>, <code>\)</code><br> <code>\~</code>, <code>\#</code>, <code>\+</code>, <code>\-</code>.</li>
  <li>الهدف هو تقديم محتوى احترافي دون أي أخطاء تنسيقية.</li>
  <li>قم بمراجعة كل النصوص قبل إرسالها، وإذا كان النص يحتوي على مشكلة في التنسيق، أرسله بدون تنسيق مع الاعتذار.</li>
</ul>
''',
    
    "course_info": {
        "name": "Python Basics",
        "duration_weeks": 16,
        "lessons_per_week": 1,
        "lesson_duration_hours": 2,
        "level": "مبتدئ",
        "group_link": "https://t.me/+gVcWKBI6ZeY1ZGY0",
        "lessons": {
            "الدرس 1": {
                "title": "مقدمة إلى بايثون وإعداد البيئة",
                "description": """
                • تعريف لغة بايثون ومميزاتها
                • مجالات استخدام بايثون
                • تثبيت بايثون على نظام التشغيل
                • تثبيت PyCharm IDE
                • كتابة أول برنامج Hello World
                • شرح بنية الكود في بايثون
                """
            },
            "الدرس 2": {
                "title": "المتغيرات وأنواع البيانات",
                "description": """
                • تعريف المتغيرات وقواعد تسميتها
                • الأنواع الأساسية: int, float, string, boolean
                • التحويل بين أنواع البيانات
                • العمليات الحسابية والمنطقية
                • الدوال المدمجة مثل print و input
                • التعامل مع النصوص وعمليات السلاسل النصية
                """
            },
            "الدرس 3": {
                "title": "الجمل الشرطية",
                "description": """
                • مفهوم الشروط في البرمجة
                • استخدام if, elif, else
                • المقارنات المنطقية (==, !=, >, <)
                • العوامل المنطقية (and, or, not)
                • الشروط المتداخلة
                • تطبيقات عملية على الشروط
                """
            },
            "الدرس 4": {
                "title": "الحلقات التكرارية",
                "description": """
                • مفهوم التكرار في البرمجة
                • حلقة while وشروط توقفها
                • حلقة for وكيفية استخدامها
                • دالة range وخصائصها
                • استخدام break و continue
                • تطبيقات على الحلقات التكرارية
                """
            },
            "الدرس 5": {
                "title": "القوائم - الجزء الأول",
                "description": """
                • مفهوم القوائم وأهميتها
                • إنشاء وتعديل القوائم
                • الوصول لعناصر القائمة وتغييرها
                • الدوال الأساسية للقوائم (append, insert, remove)
                • التقطيع في القوائم
                • نسخ القوائم والتعامل مع المراجع
                """
            },
            "الدرس 6": {
                "title": "القوائم مع الحلقات",
                "description": """
                • استخدام for مع القوائم
                • البحث في القوائم
                • الفرز والترتيب
                • List Comprehension
                • تطبيقات متقدمة على القوائم
                • معالجة البيانات في القوائم
                """
            },
            "الدرس 7": {
                "title": "الدوال",
                "description": """
                • تعريف وإنشاء الدوال
                • المعاملات والقيم الافتراضية
                • إرجاع القيم من الدوال
                • المتغيرات المحلية والعامة
                • التوثيق وأفضل الممارسات
                • الدوال المتداخلة والمتكررة
                """
            },
            "الدرس 8": {
                "title": "التعامل مع الملفات",
                "description": """
                • قراءة وكتابة الملفات النصية
                • أوضاع فتح الملفات
                • التعامل مع المسارات
                • معالجة الأخطاء في الملفات
                • العمل مع CSV
                • أفضل ممارسات التعامل مع الملفات
                """
            },
            "الدرس 9": {
                "title": "القواميس والمجموعات",
                "description": """
                • مفهوم القواميس وبنيتها
                • إنشاء وتعديل القواميس
                • الوصول للمفاتيح والقيم
                • المجموعات وعملياتها
                • تطبيقات على القواميس
                • استخدام القواميس في معالجة البيانات
                """
            },
            "الدرس 10": {
                "title": "معالجة الأخطاء",
                "description": """
                • مفهوم الاستثناءات
                • استخدام try و except
                • أنواع الاستثناءات المختلفة
                • finally و else في معالجة الأخطاء
                • إنشاء استثناءات مخصصة
                • أفضل ممارسات معالجة الأخطاء
                """
            },
            "الدرس 11": {
                "title": "البرمجة كائنية التوجه - الجزء الأول",
                "description": """
                • مفهوم OOP وأهميته
                • تعريف الفئات والكائنات
                • المتغيرات والدوال داخل الفئات
                • الدالة __init__
                • الخصائص والطرق
                • التغليف وإخفاء البيانات
                """
            },
            "الدرس 12": {
                "title": "البرمجة كائنية التوجه - الجزء الثاني",
                "description": """
                • الوراثة وأنواعها
                • تعدد الأشكال
                • الدوال الخاصة في بايثون
                • التجريد والواجهات
                • أنماط التصميم الأساسية
                • تطبيقات عملية على OOP
                """
            }
        }
    },
    
    "schedule": {
        "days": ["السبت"],
        "time": "6:00 مساءً",
        "duration": "ساعتين",
        "timezone": "توقيت القاهرة",
        "location": "أونلاين عبر Zoom"
    },

    "instructors": [
        {
            "name": "عثمان مصطفى النحراوي",
            "title": "مدرب",
            "telegram": "@CodroCourse",
            "phone": "01062385475"
        },
        {
            "name": "يوسف فتحي غالي",
            "title": "مدرب",
            "telegram": "@yousefghaly",
            "phone": "01023592779"
        }
    ],
}