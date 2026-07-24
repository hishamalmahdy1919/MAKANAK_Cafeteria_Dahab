# -*- coding: utf-8 -*-
import os

OUT = "."

# روابط الاتصال والسوشيال ميديا الخاصة بك
SITE_URL = "https://www.planetdivers.com"
EMAIL = "ahmedtahasayed@gmail.com"
WHATSAPP = "+201110111549"
WHATSAPP_LINK = "https://wa.me/201110111549"
FACEBOOK_LINK = "https://www.facebook.com/share/1BmH81bbUH/"
TIKTOK_LINK = "https://www.tiktok.com/@ahmedtaha5222?_r=1&_t=ZS-9883zJjl3cT"
LOCATION_LINK = "https://maps.app.goo.gl/YeLti1DH81tJYVQF9?g_st=aw"
GOOGLE_LINK = "https://share.google/L3e6XGfntB44pETMQ"
INSTAGRAM_LINK = "https://www.instagram.com/atsmiabo?igsh=MXU1aW1ydHN0MGdsdg=="

# عنوان إنستاباي
INSTAPAY_ADDRESS = "ahmed.taha.sayed@instapay"

# ==================================================================== #
# 1. صور وجمل العرض المتداخلة (Slideshow)
# ==================================================================== #
HERO_SLIDES = [
    {
        "image": "hero-slide1.jpg",
        "text": {
            "en": "Explore the Blue Hole", "ar": "استكشف أعماق البلوهول",
            "ru": "Исследуйте Голубую дыру", "it": "Esplora il Blue Hole",
            "fr": "Explorez le Blue Hole", "de": "Entdecke das Blue Hole",
            "zh": "探索蓝洞", "es": "Explora el Blue Hole"
        }
    },
    {
        "image": "hero-slide2.jpg",
        "text": {
            "en": "Master Your Breath", "ar": "تحكم في أنفاسك",
            "ru": "Овладейте своим дыханием", "it": "Padroneggia il respiro",
            "fr": "Maîtrisez votre souffle", "de": "Meistere deinen Atem",
            "zh": "掌控呼吸", "es": "Domina tu respiración"
        }
    },
    {
        "image": "hero-slide3.jpg",
        "text": {
            "en": "Dive with Professionals", "ar": "غُص مع المحترفين",
            "ru": "Погружайтесь с профи", "it": "Immergiti con i professionisti",
            "fr": "Plongez avec les pros", "de": "Tauche mit Profis",
            "zh": "与专家潜水", "es": "Bucea con profesionales"
        }
    },
    {
        "image": "hero-slide4.jpg",
        "text": {
            "en": "Relax at Our Cafeteria", "ar": "استرخِ في الكافيه الخاص بنا",
            "ru": "Отдохните в нашем кафе", "it": "Rilassati nella nostra caffetteria",
            "fr": "Détendez-vous à notre cafétéria", "de": "Entspannen Sie in unserer Cafeteria",
            "zh": "在我们的咖啡厅放松", "es": "Relájate en nuestra cafetería"
        }
    },
    {
        "image": "hero-slide5.jpg",
        "text": {
            "en": "Discover the Red Sea", "ar": "اكتشف سحر البحر الأحمر",
            "ru": "Откройте для себя Красное море", "it": "Scopri il Mar Rosso",
            "fr": "Découvrez la mer Rouge", "de": "Entdecken Sie das Rote Meer",
            "zh": "探索红海", "es": "Descubre el Mar Rojo"
        }
    },
    {
        "image": "hero-slide6.jpg",
        "text": {
            "en": "Unforgettable Experience", "ar": "تجربة لا تُنسى",
            "ru": "Незабываемый опыт", "it": "Esperienza indimenticabile",
            "fr": "Expérience inoubliable", "de": "Unvergessliches Erlebnis",
            "zh": "难忘的经历", "es": "Experiencia inolvidable"
        }
    },
    {
        "image": "hero-slide7.jpg",
        "text": {
            "en": "Expert Instructors", "ar": "مدربون خبراء",
            "ru": "Опытные инструкторы", "it": "Istruttori esperti",
            "fr": "Instructeurs experts", "de": "Erfahrene Ausbilder",
            "zh": "专家教练", "es": "Instructores expertos"
        }
    },
    {
        "image": "hero-slide8.jpg",
        "text": {
            "en": "Join Our Community", "ar": "انضم إلى مجتمع الغواصين",
            "ru": "Присоединяйтесь к нашему сообществу", "it": "Unisciti alla nostra community",
            "fr": "Rejoignez notre communauté", "de": "Treten Sie unserer Gemeinschaft bei",
            "zh": "加入我们的社区", "es": "Únete a nuestra comunidad"
        }
    }
]

# ==================================================================== #
# 2. الفيديوهات المحلية ورحلات السفاري
# ==================================================================== #
LOCAL_SHORTS = [
    "short-1.mp4", "short-2.mp4", "short-3.mp4",
    "short-4.mp4", "short-5.mp4", "short-6.mp4",
]

SAFARI_TRIPS = [
    {
        "image": "safari-1.jpg",
        "title": {"ar": "سهرة وادي قني", "en": "Wadi Qnai Evening Night"},
        "lines": {
            "ar": ["شاملة ذهاب وعودة", "وجبة ربع فراخ مشوية وعيش وسلطة وطحينة", "السعر 550 LE"],
            "en": ["Includes round trip", "1/4 Grilled chicken meal, bread, salad & tahini", "Price: 550 LE"]
        }
    },
    {
        "image": "safari-2.jpg",
        "title": {"ar": "رحلة لاجونا", "en": "Laguna Trip"},
        "lines": {
            "ar": ["شاملة ذهاب وعودة", "وجبة ربع فراخ مشوية وعيش وسلطة وطحينة", "السعر 450 LE"],
            "en": ["Includes round trip", "1/4 Grilled chicken meal, bread, salad & tahini", "Price: 450 LE"]
        }
    },
    {
        "image": "safari-3.jpg",
        "title": {"ar": "رحلة ال ٣ بولز", "en": "3 Pools Trip"},
        "lines": {
            "ar": ["شاملة ذهاب وعودة", "سنوركلينج", "المرشد", "بيتش باجي", "السعر 800 LE"],
            "en": ["Includes round trip", "Snorkeling", "Guide included", "Beach Buggy (ATV)", "Price: 800 LE"]
        }
    },
    {
        "image": "safari-4.jpg",
        "title": {"ar": "رحلة سفاري بيتش باجي", "en": "Beach Buggy Safari"},
        "lines": {
            "ar": ["ذهاب إلى البانوراما ثم جبل الطويلات ثم لاجونا", "السعر مصريين single 750 LE / Double 900 LE", "أجنبي 25$"],
            "en": ["Panorama, Twaylat Mountain, then Laguna", "Egyptians: Single 750 LE / Double 900 LE", "Foreigners: 25$"]
        }
    },
    {
        "image": "safari-5.jpg",
        "title": {"ar": "رحلة اليخت", "en": "Yacht Trip"},
        "lines": {
            "ar": ["صباحاً: من ٩ صباحاً إلى ٣ عصراً", "السعر: 1000 مصريين / 30$ أجنبي", "مسائي: من ٤ عصراً إلى ٩ مساءً", "السعر: 900 مصريين / 25$ أجنبي", "الغواصة: 500 مصريين / 25$ أجنبي"],
            "en": ["Morning: 9 AM - 3 PM", "Price: 1000 EGP (Egyptians) / 30$ (Foreigners)", "Evening: 4 PM - 9 PM", "Price: 900 EGP (Egyptians) / 25$ (Foreigners)", "Submarine: 500 EGP (Egyptians) / 25$ (Foreigners)"]
        }
    },
    {
        "image": "safari-6.jpg",
        "title": {"ar": "رحلة الجبل", "en": "Mountain Trip"},
        "lines": {
            "ar": ["شاملة ذهاب وعودة", "٢ شو راقصة (الراقصة وعد) + (راقصة أخرى)", "فاير شو", "تنورة", "عزف عود", "السعر 250 LE"],
            "en": ["Includes round trip", "2 Belly Dance Shows", "Fire Show", "Tanoura Show", "Oud Music", "Price: 250 LE"]
        }
    },
    {
        "image": "safari-7.jpg",
        "title": {"ar": "أطول رحلة بيتش باجي في مدينة دهب", "en": "Longest ATV Safari in Dahab"},
        "lines": {
            "ar": ["شاملة ركوب بيتش باجي من اللايت هاوس إلى البلو هول", "وقفة للتصوير مع الجمال", "شامل تيكيت دخول محمية البلو هول", "سنوركلينج", "الرجوع من البلو هول إلى اللايت هاوس بالبيتش باجي", "السعر: دبل 1500 LE / سنجل 1200 LE", "الأجانب يضاف 20$ دخول محمية البلو هول"],
            "en": ["ATV ride from Lighthouse to Blue Hole", "Stop for photos with camels", "Includes Blue Hole National Park ticket", "Snorkeling", "Return by ATV to Lighthouse", "Price: Double 1500 LE / Single 1200 LE", "Foreigners: Add 20$ for Blue Hole ticket"]
        }
    },
    {
        "image": "safari-8.jpg",
        "title": {"ar": "رحلة أبو جالوم + بلو هول + بلو لاجون", "en": "Abu Galum + Blue Hole + Blue Lagoon"},
        "lines": {
            "ar": ["الذهاب بالمركب", "الانتقال بالسيارة إلى أبو جالوم", "ممارسة سنوركلينج + Drink", "الانتقال بالسيارة إلى محمية بلو لاجون", "ممارسة سنوركلينج + Drink", "العودة إلى المركب ثم العودة إلى البلو هول", "سنوركلينج", "وجبة غداء ربع فراخ مشوية وعيش وسلطة وطحينة", "شاملة لايف جاكيت + حذاء"],
            "en": ["Boat ride", "Car transfer to Abu Galum", "Snorkeling + Drink", "Car transfer to Blue Lagoon", "Snorkeling + Drink", "Return to boat, then to Blue Hole", "Snorkeling", "Lunch: 1/4 Grilled chicken meal", "Includes Life Jacket + Water Shoes"]
        }
    }
]

# ==================================================================== #
COURSES = [
    {"course": "AIDA 1", "days": 2, "price": 200},
    {"course": "AIDA 2", "days": 3, "price": 290},
    {"course": "AIDA 3", "days": 4, "price": 340},
    {"course": "AIDA 4", "days": 5, "price": 450},
]
ACCOM_DEDUCT = [
    {"course": "AIDA 1", "discount": 25},
    {"course": "AIDA 2", "discount": 40},
    {"course": "AIDA 3", "discount": 50},
    {"course": "AIDA 4", "discount": 60},
]
CROSSOVER = [
    {"course": "AIDA 2", "discount": 80},
    {"course": "AIDA 3", "discount": 100},
    {"course": "AIDA 4", "discount": 110},
]

LANGS = ["en", "ar", "ru", "it", "fr", "de", "zh", "es"]
FILENAME = {"en": "index.html", "ar": "ar.html", "ru": "ru.html", "it": "it.html",
            "fr": "fr.html", "de": "de.html", "zh": "zh.html", "es": "es.html"}
HREFLANG = {"en": "en", "ar": "ar", "ru": "ru", "it": "it", "fr": "fr", "de": "de", "zh": "zh-Hans", "es": "es"}

# ----------------- القاموس الشامل (مضاف إليه ترجمات الحجز بالكامل) -----------------
T = {
 "en": dict(label="English", dir="ltr",
   nav_home="Home", nav_courses="Courses", nav_includes="What's Included", nav_crossover="Crossover",
   nav_videos="Videos", nav_safari="Safari", nav_contact="Contact",
   page_title="MAKANAK | Freediving Courses",
   meta_desc="Discover MAKANAK in Dahab: Cafe, restaurant, and professional freediving courses. Safari trips, Blue Hole, snorkeling, and Red Sea activities.",
   meta_keywords="Blue Hole, Dahab, Safari, Trips, Red Sea, Travel, Egypt, Sea, Diving, Freediving, Snorkeling, Cafe, Restaurant, Makanak, Abu Galum, Blue Lagoon, Twaylat Mountain, Sharm El Sheikh, Boat trips, Yacht, Dahab protectorates, Dahab restaurants, Dahab outings, Dahab nightlife, Dahab activities",
   why_title="Why Choose Our Courses?", why_items=["Professional instruction", "Small groups", "Safety training", "Equipment included", "Photos/videos", "AIDA certification"],
   courses_title="Courses & Pricing", th_course="Course", th_days="Days", th_price="Price", th_discount="Discount",
   includes_title="What the Course Includes", practical_title="Practical Training", practical_accommodation="Accommodation included",
   practical_items=["5 Open Water Sessions", "2 Pool Sessions", "Training in three different equalization techniques", "Breathing techniques for freediving", "Efficient and comfortable diving methods to reduce physical stress and increase performance", "Safety procedures in open water", "Rescue techniques from depth to the surface"],
   theory_title="Theory Lessons", theory_desc="Comprehensive theory classes covering the essential aspects of freediving, including:", theory_items=["Physiology", "Physics", "Nutrition", "Freediving safety and best practices"],
   additional_title="Additional Benefits", additional_items=["Full use of all freediving equipment", "Underwater photos and videos during the course"],
   excluded_title="Excluded Fees", excluded_intro="The following fees are not included in the course price:", excluded_items=["AIDA Certification Fee: €20 (paid upon successful course completion)", "Blue Hole National Park Entrance Fee: $30"],
   accommodation_note_title="Course without accommodation deduct as follows:", crossover_title="Crossover Programs", crossover_desc="For certified freedivers wishing to transfer from another recognized organization to AIDA at the same certification level.", crossover_discount_title="Crossover Discounts",
   closing_line="Start your freediving journey in Dahab and discover the underwater world with confidence and safety.",
   shorts_title="SCUBA & FREE DIVING", shorts_empty="Videos coming soon.",
   safari_title="Safari & Trips", safari_empty="Trips coming soon.",
   contact_title="Contact Us", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="Location", tooltip_google="Google", tooltip_email="Email", tooltip_wa="WhatsApp", tooltip_menu="Food & Drink Menu", tooltip_ig="Instagram",
   booking_form_title="Book Safari Trip", booking_date="Trip Date:", booking_name="Full Name:", booking_phone="Phone Number:", booking_wa="WhatsApp Number:", booking_btn="Done (Confirm Booking)", instapay_btn="Pay via InstaPay", toast_msg="InstaPay address copied successfully!",
   footer_text="MAKANAK.", og_locale="en_US"),

 "ar": dict(label="العربية", dir="rtl",
   nav_home="الرئيسية", nav_courses="الكورسات", nav_includes="ما يشمله الكورس", nav_crossover="التحويل",
   nav_videos="فيديوهات", nav_safari="سفاري", nav_contact="اتصل بنا",
   page_title="مكانك | كورسات الغطس الحر",
   meta_desc="اكتشف مكانك في دهب: كافيه، مطعم، وكورسات غطس حر احترافية. رحلات سفاري، بلوهول، سنوركلينج، وأفضل الأنشطة في البحر الأحمر.",
   meta_keywords="بلوهول, دهب, سفاري, رحلات, البحر الاحمر, السفر, مصر, البحر, الغوص, الغوص الحر, سنوركلينج, كافيه, مطعم, مكانك, محميه ابو جالوم, بلو لاجون, جبل الطويلات, شرم الشيخ, رحلات بحريه, يخت, محميات دهب, مطاعم دهب, خروجات دهب, السهر في دهب, الانشطه في دهب",
   why_title="لماذا تختار كورساتنا؟", why_items=["تدريب احترافي", "مجموعات صغيرة", "تدريب أمان", "المعدات متضمنة", "صور/فيديو", "شهادة AIDA"],
   courses_title="الأسعار", th_course="الكورس", th_days="الأيام", th_price="السعر", th_discount="الخصم",
   includes_title="ما يشمله الكورس", practical_title="التدريب العملي", practical_accommodation="الإقامة متضمنة",
   practical_items=["5 جلسات مياه مفتوحة", "جلستان في المسبح", "التدريب على ثلاث تقنيات مختلفة لموازنة الضغط", "تقنيات التنفس للغطس الحر", "أساليب غطس فعّالة ومريحة", "إجراءات الأمان في المياه المفتوحة", "تقنيات الإنقاذ"],
   theory_title="الدروس النظرية", theory_desc="محاضرات نظرية شاملة تغطي أهم جوانب الغطس الحر، تشمل:", theory_items=["علم وظائف الأعضاء", "الفيزياء", "التغذية", "أمان الغطس الحر وأفضل الممارسات"],
   additional_title="مزايا إضافية", additional_items=["استخدام كامل لجميع معدات الغطس الحر", "صور وفيديوهات تحت الماء أثناء الكورس"],
   excluded_title="رسوم غير متضمنة", excluded_intro="الرسوم التالية غير متضمنة في سعر الكورس:", excluded_items=["رسوم شهادة AIDA: 20 يورو", "رسوم دخول محمية البلوهول: 30 دولار"],
   accommodation_note_title="الكورس بدون إقامة يُخصم كالتالي:", crossover_title="برنامج التحويل", crossover_desc="للغطاسين الحاصلين على شهادات ويرغبون في التحويل إلى AIDA.", crossover_discount_title="خصومات التحويل",
   closing_line="ابدأ رحلتك في الغوص بدهب واكتشف عالم ما تحت الماء بثقة وأمان.",
   shorts_title="سكوبا وغطس حر", shorts_empty="قريباً.",
   safari_title="رحلات وسفاري", safari_empty="قريباً.",
   contact_title="تواصل معنا", contact_cta="واتساب", contact_email_label="البريد", contact_whatsapp_label="واتساب",
   tooltip_fb="فيسبوك", tooltip_tiktok="تيك توك", tooltip_location="الموقع", tooltip_google="جوجل", tooltip_email="بريد إلكتروني", tooltip_wa="واتساب", tooltip_menu="منيو الطعام والمشروبات", tooltip_ig="إنستجرام",
   booking_form_title="حجز رحلة سفاري", booking_date="تاريخ الرحلة:", booking_name="الاسم بالكامل:", booking_phone="رقم الهاتف:", booking_wa="رقم الواتساب:", booking_btn="تم (تأكيد الحجز)", instapay_btn="الدفع عبر إنستاباي", toast_msg="تم نسخ عنوان إنستاباي بنجاح!",
   footer_text="مكانك.", og_locale="ar_EG"),

 "ru": dict(label="Русский", dir="ltr", nav_courses="Курсы", nav_includes="Включено", nav_crossover="Кроссовер", nav_safari="Сафари", nav_contact="Контакты",
   page_title="MAKANAK | Фридайвинг", meta_desc="Дахаб.", meta_keywords="Дахаб", why_title="Почему мы?", why_items=["Профи", "Малые группы", "Безопасность", "Снаряжение", "Фото", "AIDA"],
   courses_title="Цены", th_course="Курс", th_days="Дни", th_price="Цена", th_discount="Скидка", includes_title="Включено", practical_title="Практика", practical_accommodation="Проживание", practical_items=["5 открытая вода", "2 бассейн", "Безопасность"], theory_title="Теория", theory_desc="Включает:", theory_items=["Физиология", "Физика"], additional_title="Преимущества", additional_items=["Снаряжение", "Фото"], excluded_title="Не включено", excluded_intro="Исключено:", excluded_items=["AIDA: €20", "Блю Хол: $30"], accommodation_note_title="Без проживания", crossover_title="Кроссовер", crossover_desc="Переход в AIDA.", crossover_discount_title="Скидки", closing_line="Начни сейчас.",
   shorts_title="СКУБА И ФРИДАЙВИНГ", shorts_empty="Скоро.", safari_title="Сафари", safari_empty="Скоро.", contact_title="Свяжитесь с нами", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="Локация", tooltip_google="Google", tooltip_email="Email", tooltip_wa="WhatsApp", tooltip_menu="Меню", tooltip_ig="Instagram",
   booking_form_title="Забронировать сафари", booking_date="Дата поездки:", booking_name="Полное имя:", booking_phone="Номер телефона:", booking_wa="Номер WhatsApp:", booking_btn="Готово (Подтвердить)", instapay_btn="Оплатить через InstaPay", toast_msg="Адрес InstaPay скопирован!",
   footer_text="MAKANAK.", og_locale="ru_RU"),

 "it": dict(label="Italiano", dir="ltr", nav_courses="Corsi", nav_includes="Incluso", nav_crossover="Crossover", nav_safari="Safari", nav_contact="Contatti",
   page_title="MAKANAK | Apnea", meta_desc="Apnea a Dahab.", meta_keywords="apnea Dahab", why_title="Perché noi?", why_items=["Pro", "Sicurezza", "AIDA"], courses_title="Prezzi", th_course="Corso", th_days="Giorni", th_price="Prezzo", th_discount="Sconto", includes_title="Incluso", practical_title="Pratica", practical_accommodation="Alloggio", practical_items=["5 mare", "2 piscina"], theory_title="Teoria", theory_desc="Include:", theory_items=["Fisiologia", "Fisica"], additional_title="Vantaggi", additional_items=["Attrezzatura", "Foto/video"], excluded_title="Escluso", excluded_intro="Escluso:", excluded_items=["AIDA: €20", "Blue Hole: $30"], accommodation_note_title="Senza alloggio", crossover_title="Crossover", crossover_desc="Passaggio AIDA.", crossover_discount_title="Sconti", closing_line="Inizia ora.",
   shorts_title="SCUBA & APNEA", shorts_empty="In arrivo.", safari_title="Safari", safari_empty="In arrivo.", contact_title="Contattaci", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="Posizione", tooltip_google="Google", tooltip_email="Email", tooltip_wa="WhatsApp", tooltip_menu="Menù", tooltip_ig="Instagram",
   booking_form_title="Prenota Safari", booking_date="Data del viaggio:", booking_name="Nome e cognome:", booking_phone="Numero di telefono:", booking_wa="Numero WhatsApp:", booking_btn="Fatto (Conferma)", instapay_btn="Paga tramite InstaPay", toast_msg="Indirizzo InstaPay copiato!",
   footer_text="MAKANAK.", og_locale="it_IT"),

 "fr": dict(label="Français", dir="ltr", nav_courses="Cours", nav_includes="Inclus", nav_crossover="Crossover", nav_safari="Safari", nav_contact="Contact",
   page_title="MAKANAK | Apnée", meta_desc="Apnée à Dahab.", meta_keywords="apnée", why_title="Pourquoi nous ?", why_items=["Pro", "Sécurité", "AIDA"], courses_title="Tarifs", th_course="Cours", th_days="Jours", th_price="Prix", th_discount="Réduction", includes_title="Inclus", practical_title="Pratique", practical_accommodation="Hébergement", practical_items=["5 mer", "2 piscine"], theory_title="Théorie", theory_desc="Inclus:", theory_items=["Physiologie"], additional_title="Avantages", additional_items=["Équipement"], excluded_title="Exclus", excluded_intro="Exclus:", excluded_items=["AIDA: 20€", "Blue Hole: 30$"], accommodation_note_title="Sans hébergement", crossover_title="Crossover", crossover_desc="Passage AIDA.", crossover_discount_title="Réductions", closing_line="Commencez.",
   shorts_title="PLONGÉE & APNÉE", shorts_empty="À venir.", safari_title="Safari", safari_empty="À venir.", contact_title="Contact", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="Emplacement", tooltip_google="Google", tooltip_email="Email", tooltip_wa="WhatsApp", tooltip_menu="Menu", tooltip_ig="Instagram",
   booking_form_title="Réserver un Safari", booking_date="Date du voyage :", booking_name="Nom complet :", booking_phone="Numéro de téléphone :", booking_wa="Numéro WhatsApp :", booking_btn="Terminé (Confirmer)", instapay_btn="Payer via InstaPay", toast_msg="Adresse InstaPay copiée !",
   footer_text="MAKANAK.", og_locale="fr_FR"),

 "de": dict(label="Deutsch", dir="ltr", nav_courses="Kurse", nav_includes="Inklusive", nav_crossover="Crossover", nav_safari="Safari", nav_contact="Kontakt",
   page_title="MAKANAK | Apnoetauchen", meta_desc="Dahab.", meta_keywords="Dahab", why_title="Warum wir?", why_items=["Profi", "Sicherheit"], courses_title="Preise", th_course="Kurs", th_days="Tage", th_price="Preis", th_discount="Rabatt", includes_title="Inklusive", practical_title="Praxis", practical_accommodation="Unterkunft", practical_items=["5 Freiwasser"], theory_title="Theorie", theory_desc="Inhalt:", theory_items=["Physiologie"], additional_title="Vorteile", additional_items=["Ausrüstung"], excluded_title="Exklusiv", excluded_intro="Nicht enthalten:", excluded_items=["AIDA: 20€", "Blue Hole: 30$"], accommodation_note_title="Ohne Unterkunft", crossover_title="Crossover", crossover_desc="Wechsel zu AIDA.", crossover_discount_title="Rabatte", closing_line="Starte jetzt.",
   shorts_title="GERÄTETAUCHEN & APNOE", shorts_empty="Bald.", safari_title="Safari", safari_empty="Bald.", contact_title="Kontakt", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="Standort", tooltip_google="Google", tooltip_email="E-Mail", tooltip_wa="WhatsApp", tooltip_menu="Speisekarte", tooltip_ig="Instagram",
   booking_form_title="Safari Buchen", booking_date="Reisedatum:", booking_name="Vollständiger Name:", booking_phone="Telefonnummer:", booking_wa="WhatsApp-Nummer:", booking_btn="Fertig (Bestätigen)", instapay_btn="Mit InstaPay bezahlen", toast_msg="InstaPay-Adresse kopiert!",
   footer_text="MAKANAK.", og_locale="de_DE"),

 "zh": dict(label="中文", dir="ltr", nav_courses="课程", nav_includes="包含", nav_crossover="转换", nav_safari="游猎", nav_contact="联系",
   page_title="MAKANAK | 自由潜水", meta_desc="达哈布.", meta_keywords="达哈布", why_title="为什么选我们?", why_items=["专业", "安全"], courses_title="价格", th_course="课程", th_days="天", th_price="价格", th_discount="折扣", includes_title="包含", practical_title="实践", practical_accommodation="含住宿", practical_items=["5次海潜"], theory_title="理论", theory_desc="包括:", theory_items=["生理"], additional_title="福利", additional_items=["装备"], excluded_title="不含", excluded_intro="不含:", excluded_items=["AIDA: €20", "蓝洞: $30"], accommodation_note_title="不含住宿", crossover_title="转换", crossover_desc="转至AIDA.", crossover_discount_title="折扣", closing_line="开始吧.",
   shorts_title="水肺潜水 & 自由潜水", shorts_empty="即将推出.", safari_title="游猎", safari_empty="即将推出.", contact_title="联系", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="位置", tooltip_google="Google", tooltip_email="电子邮件", tooltip_wa="WhatsApp", tooltip_menu="菜单", tooltip_ig="Instagram",
   booking_form_title="预订游猎行程", booking_date="行程日期:", booking_name="姓名:", booking_phone="电话号码:", booking_wa="WhatsApp号码:", booking_btn="完成 (确认预订)", instapay_btn="通过InstaPay付款", toast_msg="InstaPay地址已复制！",
   footer_text="MAKANAK.", og_locale="zh_CN"),

 "es": dict(label="Español", dir="ltr", nav_courses="Cursos", nav_includes="Incluido", nav_crossover="Crossover", nav_safari="Safari", nav_contact="Contacto",
   page_title="MAKANAK | Apnea", meta_desc="Dahab.", meta_keywords="Dahab", why_title="¿Por qué nosotros?", why_items=["Pro", "Seguridad"], courses_title="Precios", th_course="Curso", th_days="Días", th_price="Precio", th_discount="Descuento", includes_title="Incluido", practical_title="Práctica", practical_accommodation="Alojamiento", practical_items=["5 mar"], theory_title="Teoría", theory_desc="Incluye:", theory_items=["Fisiología"], additional_title="Beneficios", additional_items=["Equipo"], excluded_title="Excluido", excluded_intro="Excluido:", excluded_items=["AIDA: 20€", "Blue Hole: 30$"], accommodation_note_title="Sin alojamiento", crossover_title="Crossover", crossover_desc="Paso a AIDA.", crossover_discount_title="Descuentos", closing_line="Empieza ya.",
   shorts_title="BUCEO Y APNEA", shorts_empty="Pronto.", safari_title="Safari", safari_empty="Pronto.", contact_title="Contacto", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   tooltip_fb="Facebook", tooltip_tiktok="TikTok", tooltip_location="Ubicación", tooltip_google="Google", tooltip_email="Correo", tooltip_wa="WhatsApp", tooltip_menu="Menú", tooltip_ig="Instagram",
   booking_form_title="Reservar Safari", booking_date="Fecha del viaje:", booking_name="Nombre completo:", booking_phone="Número de teléfono:", booking_wa="Número de WhatsApp:", booking_btn="Hecho (Confirmar)", instapay_btn="Pagar con InstaPay", toast_msg="¡Dirección InstaPay copiada!",
   footer_text="MAKANAK.", og_locale="es_ES"),
}

def esc(s):
    return str(s).replace("&", "&").replace("<", "<").replace(">", ">")

def price_table(headers, rows):
    thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="price-table"><thead><tr>{thead}</tr></thead><tbody>{trs}</tbody></table>'

def bullet_list(items):
    return '<ul class="bullets">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"

def why_cards(items):
    cards = "".join(f'<div class="why-card"><span class="check">✓</span><p>{esc(i)}</p></div>' for i in items)
    return f'<div class="why-grid">{cards}</div>'

def hreflang_tags(current):
    tags = [f'<link rel="alternate" hreflang="{HREFLANG[lg]}" href="{SITE_URL}/{FILENAME[lg]}">' for lg in LANGS]
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/index.html">')
    return "".join(tags)

def lang_switcher(current):
    opts = []
    for lg in LANGS:
        active_class = ' class="active"' if lg == current else ''
        opts.append('<a href="' + FILENAME[lg] + '"' + active_class + ' hreflang="' + HREFLANG[lg] + '">' + T[lg]["label"] + '</a>')

    opts_str = "".join(opts)
    btn = '<button class="lang-toggle" aria-label="Language" onclick="document.getElementById(' + "'langMenu'" + ').classList.toggle(' + "'open'" + ')">🌐 ' + T[current]["label"] + '</button>'
    return '<div class="lang-switcher">' + btn + '<div class="lang-menu" id="langMenu">' + opts_str + '</div></div>'

def nav_links(t):
    return f'<a href="#courses">{esc(t.get("nav_courses", ""))}</a><a href="#includes">{esc(t.get("nav_includes", ""))}</a><a href="#crossover">{esc(t.get("nav_crossover", ""))}</a><a href="#shorts">{esc(t.get("shorts_title", ""))}</a><a href="#safari">{esc(t.get("nav_safari", ""))}</a><a href="#contact">{esc(t.get("nav_contact", ""))}</a>'

def social_links(t):
    return f"""
    <div class="social-hero">
      <a href="{FACEBOOK_LINK}" target="_blank" class="tooltip-container" aria-label="Facebook">
        <i class="fab fa-facebook-f"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_fb', 'Facebook'))}</span>
      </a>
      <a href="{INSTAGRAM_LINK}" target="_blank" class="tooltip-container" aria-label="Instagram">
        <i class="fab fa-instagram"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_ig', 'Instagram'))}</span>
      </a>
      <a href="{TIKTOK_LINK}" target="_blank" class="tooltip-container" aria-label="TikTok">
        <i class="fab fa-tiktok"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_tiktok', 'TikTok'))}</span>
      </a>
      <a href="{LOCATION_LINK}" target="_blank" class="tooltip-container" aria-label="Location">
        <i class="fas fa-map-marker-alt"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_location', 'Location'))}</span>
      </a>
      <a href="{GOOGLE_LINK}" target="_blank" class="tooltip-container" aria-label="Google">
        <i class="fab fa-google"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_google', 'Google'))}</span>
      </a>
      <a href="mailto:{EMAIL}" class="tooltip-container" aria-label="Email">
        <i class="fas fa-envelope"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_email', 'Email'))}</span>
      </a>
      <a href="{WHATSAPP_LINK}" target="_blank" class="tooltip-container" aria-label="WhatsApp">
        <i class="fab fa-whatsapp"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_wa', 'WhatsApp'))}</span>
      </a>
      <a href="#" onclick="openMenuLightbox(event)" class="tooltip-container menu-icon-btn" aria-label="Menu">
        <i class="fas fa-utensils"></i>
        <span class="tooltip-text">{esc(t.get('tooltip_menu', 'Menu'))}</span>
      </a>
    </div>
    """

def shorts_gallery(t):
    if not LOCAL_SHORTS: return f'<p class="videos-empty">{esc(t.get("shorts_empty", ""))}</p>'
    cards = []
    for vid in LOCAL_SHORTS:
        cards.append(f'<div class="short-card"><video src="images/{vid}" preload="metadata" controls playsinline></video></div>')
    return f'<div class="shorts-grid">{"".join(cards)}</div>'

def safari_gallery(lang):
    t = T[lang]
    cards = []
    for trip in SAFARI_TRIPS:
        title = trip["title"].get(lang, trip["title"]["en"])
        lines = trip["lines"].get(lang, trip["lines"]["en"])
        lines_html = "".join(f"<p>{esc(line)}</p>" for line in lines)
        card = f'''
        <div class="safari-card" onclick="openBooking('{esc(title)}')">
          <img src="images/{trip['image']}" alt="{esc(title)}">
          <div class="safari-info">
            <h3>{esc(title)}</h3>
            {lines_html}
            <button class="book-now-btn">{esc(t.get("booking_form_title", "Book Now"))}</button>
          </div>
        </div>
        '''
        cards.append(card)
    return f'<div class="safari-grid">{"".join(cards)}</div>'

def generate_hero_slides(lang):
    html = ""
    for i, slide in enumerate(HERO_SLIDES):
        active_class = " active" if i == 0 else ""
        img = slide["image"]
        txt = esc(slide["text"].get(lang, slide["text"]["en"]))
        bg_style = "background-image: url('images/" + img + "');"
        html += '<div class="slide slide-' + str(i+1) + active_class + '" style="' + bg_style + '">'
        html += '<div class="slide-text"><h1>' + txt + '</h1></div></div>'
    return html

def build_page(lang):
    t = T[lang]
    courses_rows = [[c["course"], c["days"], str(c["price"])] for c in COURSES]
    accom_rows = [[c["course"], str(c["discount"])] for c in ACCOM_DEDUCT]
    cross_rows = [[c["course"], str(c["discount"])] for c in CROSSOVER]

    btn_mobile = '<button class="mobile-toggle" aria-label="Menu" onclick="document.getElementById(' + "'mobileNav'" + ').classList.toggle(' + "'open'" + ')">☰</button>'

    logo_main = "مكانك" if lang == "ar" else "MAKANAK"
    logo_sub = "بلوهول دهب - كافيه وغطس حر" if lang == "ar" else "Blue hole Dahab - Cafeteria & Free Dive"

    lightbox_html = """
    <div id="menuLightbox" class="lightbox">
      <span class="close-lightbox" onclick="closeMenuLightbox()">×</span>
      <div class="lightbox-content">
        <a class="lightbox-prev" onclick="changeMenuImage(-1)">❮</a>
        <img id="lightboxImg" src="images/menu1.jpg" alt="Menu">
        <a class="lightbox-next" onclick="changeMenuImage(1)">❯</a>
      </div>
    </div>
    """

    html = f"""<!DOCTYPE html>
<html lang="{HREFLANG[lang]}" dir="{t.get("dir", "ltr")}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(t.get("page_title", ""))}</title>
<meta name="description" content="{esc(t.get("meta_desc", ""))}">
<meta name="keywords" content="{esc(t.get("meta_keywords", ""))}">
<link rel="canonical" href="{SITE_URL}/{FILENAME[lang]}">
{hreflang_tags(lang)}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="logo">
      <img src="images/logo-icon.png" alt="Logo" class="logo-icon">
      <div class="logo-text">
        <span class="logo-main">{logo_main}</span>
        <span class="logo-sub">{logo_sub}</span>
      </div>
    </a>
    <nav class="main-nav">{nav_links(t)}</nav>
    {lang_switcher(lang)}
    {btn_mobile}
  </div>
  <nav class="mobile-nav" id="mobileNav">{nav_links(t)}</nav>
</header>

<main>
  <section class="hero" id="home">
    {social_links(t)}

    <div class="hero-slideshow">
      {generate_hero_slides(lang)}
    </div>
  </section>

  <section class="section" id="shorts">
    <h2>{esc(t.get("shorts_title", ""))}</h2>
    {shorts_gallery(t)}
  </section>

  <section class="section alt" id="why">
    <h2>{esc(t.get("why_title", ""))}</h2>
    <div class="why-container">
       <div class="why-content">
          {why_cards(t.get("why_items", []))}
       </div>
       <div class="why-image-wrapper">
          <img src="images/why-divers.png" alt="Diving Professionals">
       </div>
    </div>
  </section>

  <section class="section" id="courses">
    <h2>{esc(t.get("courses_title", ""))}</h2>
    {price_table([t.get("th_course", ""), t.get("th_days", ""), t.get("th_price", "")], courses_rows)}
    <p class="note-box">(AIDA 1: 1night, AIDA 2: 2nights, AIDA 3: 3nights, AIDA 4: 4nights)</p>
  </section>

  <section class="section alt" id="includes">
    <h2>{esc(t.get("includes_title", ""))}</h2>

    <h3>🏊 {esc(t.get("practical_title", ""))}</h3>
    {bullet_list(t.get("practical_items", []))}

    <h3>📖 {esc(t.get("theory_title", ""))}</h3>
    <p>{esc(t.get("theory_desc", ""))}</p>
    {bullet_list(t.get("theory_items", []))}

    <h3>🎁 {esc(t.get("additional_title", ""))}</h3>
    {bullet_list(t.get("additional_items", []))}

    <div class="excluded-box">
      <h3>{esc(t.get("excluded_title", ""))}</h3>
      <p>{esc(t.get("excluded_intro", ""))}</p>
      {bullet_list(t.get("excluded_items", []))}
    </div>

    <h3>{esc(t.get("accommodation_note_title", ""))}</h3>
    {price_table([t.get("th_course", ""), t.get("th_discount", "")], accom_rows)}
  </section>

  <section class="section" id="safari">
    <h2>{esc(t.get("safari_title", ""))}</h2>
    {safari_gallery(lang)}
  </section>

  <section class="section alt" id="crossover">
    <h2>{esc(t.get("crossover_title", ""))}</h2>
    <p class="center-text">{esc(t.get("crossover_desc", ""))}</p>
    {price_table([t.get("th_course", ""), t.get("th_discount", "")], cross_rows)}
    <p class="closing-line">{esc(t.get("closing_line", ""))}</p>
  </section>

  <section class="section contact" id="contact">
    <h2>{esc(t.get("contact_title", ""))}</h2>
    <div class="contact-grid">
      <a class="contact-chip" href="mailto:{EMAIL}">
        <span class="chip-label">{esc(t.get("contact_email_label", ""))}</span>
        <span class="chip-value">{EMAIL}</span>
      </a>
      <a class="contact-chip" href="{WHATSAPP_LINK}" target="_blank">
        <span class="chip-label">{esc(t.get("contact_whatsapp_label", ""))}</span>
        <span class="chip-value">{WHATSAPP}</span>
      </a>
    </div>
    <a class="btn-cta" href="{WHATSAPP_LINK}" target="_blank">{esc(t.get("contact_cta", ""))}</a>
  </section>
</main>

<footer class="site-footer">
  <p>{esc(t.get("footer_text", ""))}</p>
  <p class="copyright">© <span id="year"></span> {logo_main}</p>
</footer>

{lightbox_html}

<div id="bookingModal" class="lightbox">
  <div class="lightbox-content booking-modal-content">
    <span class="close-lightbox" onclick="closeBooking()">×</span>
    <h2 id="bookingTripTitle">{esc(t.get("booking_form_title", "Book Trip"))}</h2>

    <form action="YOUR_EMAIL_LINK" method="POST" class="booking-form">
      <input type="hidden" name="Trip_Name" id="tripNameInput">

      <label>{esc(t.get("booking_date", "Date:"))}</label>
      <input type="date" name="Date" required>

      <label>{esc(t.get("booking_name", "Name:"))}</label>
      <input type="text" name="Full_Name" required>

      <label>{esc(t.get("booking_phone", "Phone:"))}</label>
      <input type="tel" name="Phone_Number" required>

      <label>{esc(t.get("booking_wa", "WhatsApp:"))}</label>
      <input type="tel" name="WhatsApp_Number" required>

      <button type="button" class="instapay-btn" onclick="copyInstaPay('{INSTAPAY_ADDRESS}')">
        <i class="fas fa-wallet"></i> {esc(t.get("instapay_btn", "Pay via InstaPay"))}
      </button>

      <button type="submit" class="btn-cta submit-btn">{esc(t.get("booking_btn", "Done"))}</button>
    </form>
  </div>
</div>

<div id="toastMessage" class="toast-msg">{esc(t.get("toast_msg", "InstaPay address copied successfully!"))}</div>

<audio id="bgMusic" src="images/bg-music.mp3" loop preload="auto"></audio>

<script src="js/script.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {{
      var audio = document.getElementById("bgMusic");
      if(audio) {{
          audio.volume = 0.15;
          var playPromise = audio.play();
          if (playPromise !== undefined) {{
              playPromise.catch(function(error) {{
                  var startAudio = function() {{
                      audio.play();
                      document.removeEventListener('click', startAudio);
                      document.removeEventListener('scroll', startAudio);
                      document.removeEventListener('touchstart', startAudio);
                  }};
                  document.addEventListener('click', startAudio);
                  document.addEventListener('scroll', startAudio);
                  document.addEventListener('touchstart', startAudio);
              }});
          }}
      }}
  }});
</script>

</body>
</html>
"""
    return html

os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
os.makedirs(os.path.join(OUT, "css"), exist_ok=True)
os.makedirs(os.path.join(OUT, "js"), exist_ok=True)

for lg in LANGS:
    path = os.path.join(OUT, FILENAME[lg])
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_page(lg))
    print("تم تحديث الصفحة:", path)