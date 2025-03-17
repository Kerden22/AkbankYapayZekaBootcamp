from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
import matplotlib.pyplot as plt
import networkx as nx

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur """

        # Başlangıç ve hedef istasyonlarının var olup olmadığını kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
              return None  # Eğer istasyonlardan biri yoksa, rota bulunamaz.
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # BFS için kuyruk oluştur (Başlangıç istasyonu ve gidilen yol listesi ile başlat)
        kuyruk = deque([(baslangic, [baslangic])])  # (mevcut istasyon, şu ana kadar gidilen yol)

        # Ziyaret edilen istasyonları takip etmek için bir küme oluştur
        ziyaret_edildi = set()
        

        # BFS Döngüsü
        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft()  # Kuyruktaki en öndeki istasyonu çıkar

            # Eğer hedef istasyona ulaştık, en az aktarmalı rota bulundu ise
            if mevcut_istasyon == hedef:
                return yol  # Bulunan en kısa istasyon listesi döndürülür
        
            # Mevcut istasyonu ziyaret edildi olarak işaretle
            ziyaret_edildi.add(mevcut_istasyon)

            # Komşuları kontrol et ve kuyruğa ekle
            for komsu, _ in mevcut_istasyon.komsular:  # Süreyi göz ardı ederek komşuları al
                if komsu not in ziyaret_edildi:
                    yeni_yol = yol + [komsu]  # Yeni rotaya komşuyu ekle
                    kuyruk.append((komsu, yeni_yol))  # Kuyruğa ekle

        # Eğer hedefe ulaşan bir yol bulunamazsa None döndür
        return None



    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur """

        # Başlangıç ve hedef istasyonlarının var olup olmadığını kontrol et
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Eğer istasyonlardan biri yoksa, rota bulunamaz.
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # A* için öncelik kuyruğu oluştur (Süre, istasyon, gidilen rota)
        pq = [(0, id(baslangic), baslangic, [baslangic])]  # (toplam süre, ID, istasyon, yol)

        # Ziyaret edilen istasyonları takip etmek için bir sözlük (istasyon: en kısa süre)
        ziyaret_edildi = {}

        # A* Döngüsü
        while pq:
            toplam_sure, _, mevcut_istasyon, yol = heapq.heappop(pq)  # En düşük süreye sahip istasyonu al

            # Eğer hedef istasyona ulaştık, en hızlı rota bulundu ise
            if mevcut_istasyon == hedef:
                return yol, toplam_sure  # (En hızlı rota, Toplam süre)

            # Eğer bu istasyon daha önce ziyaret edildiyse ve daha kısa sürede gelinemediyse, devam et
            if mevcut_istasyon in ziyaret_edildi and ziyaret_edildi[mevcut_istasyon] <= toplam_sure:
                continue

            # Mevcut istasyonu ziyaret edildi olarak işaretle
            ziyaret_edildi[mevcut_istasyon] = toplam_sure
        
            # Komşuları kontrol et ve kuyruğa ekle
            for komsu, sure in mevcut_istasyon.komsular:  # Komşu istasyonları al (süre önemli!)
                yeni_sure = toplam_sure + sure  # Toplam süreyi güncelle
                yeni_yol = yol + [komsu]  # Yeni rotaya komşuyu ekle
                heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yeni_yol))  # Öncelik kuyruğuna ekle

        # Eğer hiç rota bulunamazsa None döndür
        return None


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 


# GÖRSELLEŞTİRMELER 

def metro_agini_gorsellestir(metro: MetroAgi):
    """ Metro ağını graf olarak çizer """

    G = nx.Graph()

    # Düğümleri ekleyelim (istasyonları)
    for istasyon in metro.istasyonlar.values():
        G.add_node(istasyon.idx, label=istasyon.ad)

    # Kenarları ekleyelim (bağlantılar)
    for istasyon in metro.istasyonlar.values():
        for komsu, sure in istasyon.komsular:
            G.add_edge(istasyon.idx, komsu.idx, weight=sure)

    # Grafiği çizelim
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)  # Daha düzenli konumlandırma

    labels = {node: metro.istasyonlar[node].ad for node in G.nodes}
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}

    nx.draw(G, pos, with_labels=True, labels=labels, node_color="skyblue", node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    plt.title("Metro Ağı Görselleştirme")
    plt.show()

# Test için çağırma
metro_agini_gorsellestir(metro)


def rotayi_gorsellestir(metro: MetroAgi, rota: List[Istasyon]):
    """ Bulunan rotayı grafik üzerinde öne çıkararak gösterir """

    G = nx.Graph()

    # Düğümleri ekleyelim
    for istasyon in metro.istasyonlar.values():
        G.add_node(istasyon.idx, label=istasyon.ad)

    # Kenarları ekleyelim
    for istasyon in metro.istasyonlar.values():
        for komsu, sure in istasyon.komsular:
            G.add_edge(istasyon.idx, komsu.idx, weight=sure)

    # Grafiği çizelim
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)

    labels = {node: metro.istasyonlar[node].ad for node in G.nodes}
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}

    # Normal ağ çizimi (gri renkte arka plan olacak)
    nx.draw(G, pos, with_labels=True, labels=labels, node_color="lightgrey", node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    # Seçili rotadaki düğümleri ve kenarları vurgula
    rota_dugumleri = [istasyon.idx for istasyon in rota]
    rota_kenarlari = [(rota[i].idx, rota[i+1].idx) for i in range(len(rota)-1)]

    nx.draw_networkx_nodes(G, pos, nodelist=rota_dugumleri, node_color="red", node_size=2000)
    nx.draw_networkx_edges(G, pos, edgelist=rota_kenarlari, edge_color="red", width=2)

    plt.title("Seçili Rota Görselleştirme")
    plt.show()

# Test için bir rota bulalım ve çizdirelim
rota = metro.en_az_aktarma_bul("M1", "K4")
if rota:
    rotayi_gorsellestir(metro, rota)
