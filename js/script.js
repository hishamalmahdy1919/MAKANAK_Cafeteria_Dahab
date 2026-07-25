document.addEventListener('DOMContentLoaded', function () {
  // تحديث السنة في الفوتر
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // إغلاق قائمة اللغات عند النقر خارجها
  document.addEventListener('click', function (e) {
    var menu = document.getElementById('langMenu');
    var toggle = document.querySelector('.lang-toggle');
    if (!menu || !toggle) return;
    if (!menu.contains(e.target) && !toggle.contains(e.target)) {
      menu.classList.remove('open');
    }
  });

  // إغلاق القائمة الجانبية للموبايل عند الضغط على أي رابط
  document.querySelectorAll('.mobile-nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      document.getElementById('mobileNav').classList.remove('open');
    });
  });

  // تشغيل الـ Slideshow لصور الهيرو
  const slides = document.querySelectorAll('.hero-slideshow .slide');
  if (slides.length > 0) {
    let currentSlide = 0;
    setInterval(function() {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 5000); // تغيير الصورة كل 5 ثواني
  }
});

// -----------------------------------------------------------------
// أكواد تشغيل نافذة المنيو (Lightbox)
// -----------------------------------------------------------------
let currentMenuIndex = 0;
const menuImages = ['images/menu1.jpg', 'images/menu2.jpg'];

window.openMenuLightbox = function(e) {
  if(e) e.preventDefault();
  document.getElementById('menuLightbox').style.display = 'flex';
  document.getElementById('lightboxImg').src = menuImages[currentMenuIndex];
}

window.closeMenuLightbox = function() {
  document.getElementById('menuLightbox').style.display = 'none';
}

window.changeMenuImage = function(n) {
  currentMenuIndex += n;
  if (currentMenuIndex >= menuImages.length) {
      currentMenuIndex = 0;
  }
  if (currentMenuIndex < 0) {
      currentMenuIndex = menuImages.length - 1;
  }
  document.getElementById('lightboxImg').src = menuImages[currentMenuIndex];
}

// -----------------------------------------------------------------
// أكواد نافذة الحجز وزرار إنستاباي
// -----------------------------------------------------------------
window.openBooking = function(tripName) {
  document.getElementById('bookingModal').style.display = 'flex';
  document.getElementById('tripNameInput').value = tripName;
}

window.closeBooking = function() {
  document.getElementById('bookingModal').style.display = 'none';
}

// إغلاق النوافذ لو ضغطنا براها
window.onclick = function(event) {
  var menuLightbox = document.getElementById('menuLightbox');
  var bookingModal = document.getElementById('bookingModal');
  if (event.target == menuLightbox) { closeMenuLightbox(); }
  if (event.target == bookingModal) { closeBooking(); }
}

// وظيفة فتح تطبيق إنستاباي مباشرة (Deep Link)
window.openInstaPay = function(ipaAddress) {
  // محاولة فتح تطبيق إنستاباي مباشرة على الموبايل
  window.location.href = "instapay://";

  // إظهار رسالة للمستخدم (توضيح أنه جاري فتح التطبيق)
  var toast = document.getElementById("toastMessage");
  toast.className = "toast-msg show";
  setTimeout(function(){
    toast.className = toast.className.replace("show", "");
  }, 3000);
}