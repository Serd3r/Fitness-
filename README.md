# Fitness Rezervasyon Sistemi - Uçtan Uca Test Mühendisliği Projesi

Bu proje, "Yazılım Test Mühendisliği" dersi dönem projesi kapsamında geliştirilmiştir. FastAPI tabanlı bir REST servisidir ve TDD, Property-Based Testing, Mutasyon Testi ve Performans Testi gibi ileri düzey test tekniklerini içerir.

## 📁 Proje Dosya Yapısı ve Görevleri

Aşağıda proje içerisindeki dosyaların amaçları ve ödev gereksinimlerini nasıl karşıladığı açıklanmıştır:

### 1. Kök Dizin
*   **`README.md`**: Projenin kullanım kılavuzu ve proje özeti (Ödev Madde 6.1).
*   **`pyproject.toml`**: Proje bağımlılıklarını (FastAPI, pytest, locust vb.) ve test konfigürasyonlarını içerir (Ödev Madde 3).
*   **`Dockerfile`**: Uygulamanın konteynerize edilmesini sağlar (Ödev Madde 5.11).
*   **`docker-compose.yml`**: Proje ve bağımlılıklarını tek komutla çalıştırmak için kullanılır (Ödev Madde 5.11).
*   **`REPORT_DRAFT.md`**: Proje rapor taslağı; mimari ve test stratejilerini içerir (Ödev Madde 6.2).

### 2. Uygulama Kodu (`app/`)
Kaynak kodların bulunduğu ana dizindir.
*   **`app/main.py`**: Uygulamanın giriş noktasıdır. Router'ları bağlar, Statik Dosyaları (Frontend) ve CORS ayarlarını yapar.
*   **`app/models/`**: Veri modellerini (Pydantic şemaları) içerir.
    *   `member.py`: Üye tipleri (Standart, Premium, Öğrenci) ve validasyonları.
    *   `fitness_class.py`: Ders bilgileri.
    *   `reservation.py`: Rezervasyon şeması.
*   **`app/routers/`**: REST API uç noktaları (Endpoints) (Ödev Madde 4).
    *   `members.py`, `classes.py`, `reservations.py`: İlgili kaynaklar için CRUD işlemleri.
*   **`app/services/`**: İş mantığı katmanı.
    *   **`pricing_engine.py`**: Dinamik fiyatlandırma kuralları (Doluluk oranı, üyelik tipi vb.) (Ödev Madde 4.4 & 5.5).
    *   `reservation_service.py`: Kapasite kontrolü ve rezervasyon kaydı.

### 3. Ön Yüz (`app/static/`)
*   **`index.html`**: Sistemin kullanıcı arayüzü. Üye kaydı, ders listeleme ve rezervasyon işlemlerini görsel olarak sunar.

### 4. Testler (`tests/`)
Ödevin odak noktası olan test senaryoları buradadır (Ödev Madde 5).
*   **`tests/unit/`**: Birim testler (Ödev Madde 5.2).
    *   `test_pricing.py`: Fiyatlandırma motorunun testleri.
    *   `test_reservations.py`: Rezervasyon kurallarının testleri.
*   **`tests/property/`**: Özellik tabanlı (Property-Based) testler. `Hypothesis` kütüphanesi ile rastgele girdilerle "invariant"ların korunup korunmadığını test eder (Ödev Madde 5.6).
*   **`tests/integration/`**: Entegrasyon testleri.
    *   `postman_collection.json`: Postman/Newman ile çalıştırılabilir API test koleksiyonu (Ödev Madde 5.4).
*   **`tests/performance/`**: Yük ve Stres testleri.
    *   `locustfile.py`: `Locust` aracı ile sisteme yük bindiren senaryo (Ödev Madde 5.7).

### 5. CI/CD (`.github/workflows/`)
*   **`ci.yml`**: GitHub Actions konfigürasyonu. Her `push` işleminde testleri, lint kontrollerini ve raporlamayı otomatik yapar (Ödev Madde 5.11).

---

## 🚀 Kurulum ve Çalıştırma

### Yöntem 1: Docker (Önerilen)
Sistemi tek komutla ayağa kaldırmak için:
```bash
docker-compose up --build
```
*   **Web Arayüzü**: [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)
*   **API Dokümantasyonu**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Yöntem 2: Lokal Kurulum (Python)
Gereksinimler: Python 3.9+
1. **Bağımlılıkları Yükle**:
   ```bash
   pip install -e ".[test]"
   ```
2. **Uygulamayı Başlat**:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 Testleri Çalıştırma
Tüm test mühendisliği araçlarını aşağıdaki komutlarla çalıştırabilirsiniz:

1.  **Birim Testler ve Coverage (Kapsam)**:
    ```bash
    pytest --cov=app
    ```
    *(Beklenen kapsam: >%80)*

2.  **Performans Testi (Locust)**:
    ```bash
    locust -f tests/performance/locustfile.py
    ```
    *Tarayıcıdan http://localhost:8089 adresine giderek testi başlatın.*

3.  **Mutasyon Testi (Mutmut)**:
    ```bash
    mutmut run
    mutmut results
    ```
