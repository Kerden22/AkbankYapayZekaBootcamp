
# 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

## 📌 Proje Hakkında

Bu proje, bir metro ağı üzerinde **en az aktarmalı** ve **en hızlı** rotayı bulan bir simülasyon geliştirmeyi amaçlamaktadır. Projede iki farklı algoritma kullanılmaktadır:

-   **BFS (Breadth-First Search)** ile **en az aktarmalı rota** hesaplanmaktadır.
-   __A_ (A-Star) Algoritması_* ile **en hızlı rota** bulunmaktadır.

Metro ağı, bir **graf veri yapısı** ile modellenmiş olup, istasyonlar düğümler, istasyonlar arasındaki bağlantılar ise kenarlar olarak tanımlanmıştır. Her kenarın üzerinde bir **süre (dakika)** bulunur.

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler

Proje, Python programlama dili ile gerçekleştirilmiştir ve aşağıdaki kütüphaneler kullanılmıştır:

-   **`collections`**: **`deque`** veri yapısı ile BFS için etkin bir kuyruk yapısı oluşturmak amacıyla kullanıldı.
-   **`heapq`**: **A*** algoritmasında **öncelik kuyruğu** oluşturarak en kısa sürede hedefe ulaşmayı sağlamak için kullanıldı.
-   **`typing`**: **Fonksiyon parametreleri ve dönüş tiplerini belirlemek** amacıyla kullanıldı.

## 🔍 Algoritmaların Çalışma Mantığı

### 🔹 BFS Algoritması (En Az Aktarmalı Rota)

**BFS (Breadth-First Search)** algoritması, **katman katman ilerleyerek en az aktarmalı rotayı bulur**.

-   **Kuyruk (`deque`) kullanarak** istasyonları katman katman ziyaret eder.
-   **Ziyaret edilen istasyonlar bir kümede tutulur** ve tekrar ziyaret edilmez.
-   **Her komşunun bir adımda ziyaret edilmesi garanti edildiğinden**, hedef istasyona ulaşıldığında en az aktarmalı yol elde edilir.

### 🔹 A* Algoritması (En Hızlı Rota)

__A_ (A-Star) algoritması_*, en kısa sürede hedefe ulaşmayı sağlayan bir **optimizasyon algoritmasıdır**.

-   **Bir öncelik kuyruğu (`heapq`) kullanarak** her adımda en düşük toplam süreye sahip istasyonu işler.
-   **Ziyaret edilen istasyonlar ve en kısa sürede ulaşma bilgileri** kaydedilir.
-   **G(n) = şu ana kadar geçen süre**, **H(n) = tahmini en kısa süre** ve **F(n) = G(n) + H(n)** olarak hesaplanarak en iyi rota bulunur.

📌 **Neden Bu Algoritmalar Kullanıldı?**

-   **BFS**, en az aktarmalı rota bulmak için **ideal ve garantili** bir algoritmadır.
-   **A***, en hızlı rotayı bulmak için **optimal ve verimli** bir yaklaşımdır.

## ⚡Örnek Kullanım ve Test Sonuçları

Kodun nasıl kullanıldığına dair örnek bir test:

```python
metro = MetroAgi()
metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
metro.baglanti_ekle("M1", "K4", 10)

rota = metro.en_az_aktarma_bul("M1", "K4")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("M1", "K4")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

```

## 🚀 Projeyi Geliştirme Fikirleri

-   **Gerçek zamanlı trafik bilgisi eklenebilir.**
-   **Daha detaylı görselleştirme yapılarak** metro hatları grafiksel olarak gösterilebilir.
-   **Gerçek harita verileri ile entegre edilebilir.**
-   **Aktarma süreleri de hesaba katılarak** daha gerçekçi bir hesaplama yapılabilir.

## Mahmut Kerem Erden -  k.erden03@gmail.com
