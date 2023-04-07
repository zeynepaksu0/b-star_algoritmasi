# b-star_algoritmasi
 b* algoritmasıyla olusturulmustur ve metnin icinde istenilen keliemleri arayıp ekrana yazdırır

# KLU1210505040
python diliyle yazılmıs ve b* arama algoritmasını kullanarak arama yapan bir algoritma.

B* ARAMA ALGORİTMASI NEDİR VE NEYİ AMAÇLAR?
B* arama bir arama algoritmasıdır ve arama yaparken en kısa yolu bulmak için kullanılır. Kullanım alanları çok geniş olmasıyla birlikte genelde graph tabanlı problemleri çözmek için kullanılır ve bir düğümden başlayarak hedef düğüme een kısa ve hızlı yoldan ulaşmayı amaçlar.

 
ÇALIŞMA ŞEKLİNE BAKACAK OLURSAK;
B* arama algoritması arama yaparken, bir grafik yapısını temsil eden bir düğüm ve kenarlar ağı içinde bir başlangıc düğümü ve hedef düğümü belirler. Başlangıç düğümünden hedef düğüme ulaşana kadar her bir genişleme ağı esnasında hedefe ulaşan diğer düğümlerin maaliyetini hesaplar. Bu sayede bu algoritma, oluşturdugu baslangıc düğümünden hedef düğüme uaşan tüm yolları tek tek tarayarak hem her yolu keşfetmiş hem de kendine en hızlı bulmuş olarak algoritmayı sonlandırır.

Bu algoritmanın hedef düğüme ulaşması demek, sadece takip ettigi yolu degil, hedefe ulasan diger yolları da hesaplayarak kendi yoluyla karsılastırdıgı anlamına gelir. Zaten bu karsılastırma sayesinde en kısa yolu bulmus olur.

A* ARAMA ALGORİTMASINDAN FARKI;
B* arama algoritması, a* arama algoritması temel alınarak a* arama algoritmasının performansını iyileştirmek amacıyla oluşturulmuştur. Aralarındaki temel fark; A* arama algoritmasının önceden hesaplanılan bir tahmin üzerine en kısa yolu bulmaya çalışarak arama yaparken, B* arama algoritması a* arama algoritmasına ek maaliyet hesaplamaları yapar. Daha fazla hesaplama dücü gerektirse de daha dogru sonuc verir. Doğal olarak daha karmaşık hespalamalar için daha uygundur.

B* ARAMA ALGORİTMASININ ÇALIŞMA DURUMU;

B* arama algoritmasının çalışma zamanı, en iyi, en kötü ve ortalama durumlara göre farklılık gösterir. 
En iyi durum, algoritmanın belirlediği hedef düğüm ve başlangıç düğümünün birbirine çok yakın olduğu ve maaliyet fonksiyonu için iyi bir tahmine sahip olunulan durumdur.
En kötü durum ise, algoritmanın belirlediği hedef düğüm ve başlangıç düğümünün birbirine çok uzakta olduğu ve maliyet fonksiyonu için kötü bir tahmine sahip olunulan durumdur. 
Ortalama durum ise, algoritmanın belirlediği başlangıç ve hedef düğümlerinin arasındaki mesafenin ortalama olduğu ve maaliyet fonksiyonu için de ortalama bir tahmine sahip olunulan durumdur.

En İyi Durum:
B* arama algoritması en iyi durumda O(1) zamanında çalışır. Çünkü hedef düğüm başlangıç düğümüne çok yakın olduğu için, en kısa yolun hesaplanması çok kısa sürer. En iyi durumda, B* arama algoritmasının zaman karmaşıklığı O(1) olduğundan, zaman açısından hesaplandıgı zaman sıfıra eşdeğerdir.

En Kötü Durum:
B* arama algoritması en kötü durumda O(b^h) zamanında çalışır. Burada, b dallanma faktörü, h ise başlangıç düğümünden hedef düğüme olan maksimum yüksekliktir. Böylece, hedef düğüme ulaşmak için tüm yolların hesaplanması gerekir. 

Ortalama Durum:
B* arama algoritması ortalama durumda O(b^(h/2)) zamanında çalışır. Bu durumda, başlangıç ve hedef düğümlerinin arasındaki mesafe ortalama olduğu için, tüm yolların hesaplanması gerekebilir. 

