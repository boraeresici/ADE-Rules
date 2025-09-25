---
name: Generic ADE Rules
description: A comprehensive set of generic rules for Application Detection Engine (ADE)
version: 1.0.0
author: AI Assistant
tags: [ade, generic, rules, best-practices]
---

# Generic ADE Rules

## 1. Kod Kalitesi ve Standartları

### İsimlendirme Kuralları
- Açıklayıcı ve anlamlı isimler kullan.
- İsimlendirme kalıplarında tutarlı ol.
- Kısaltmalardan ve tek harflerden kaçın (döngü sayaçları hariç).
- Sabitler için arama yapılabilir isimler kullan.
- İsimden amacı açıkça anlaşılsın.

Örnek:
```javascript
// İyi
const MAX_RETRY_ATTEMPTS = 3;
const userAuthenticationToken = generateToken();
function calculateCompoundInterest(principal, rate, time) {}

// Kötü
const max = 3;
const tkn = generateToken();
function calc(p, r, t) {}
```

### Fonksiyon Tasarımı
- Fonksiyonları küçük ve odaklı tut (tek sorumluluk).
- Fonksiyon parametrelerini sınırla (ideal olarak 3 veya daha az).
- Eylemi belirten açıklayıcı fonksiyon isimleri kullan.
- Mümkün olduğunca yan etkilerden kaçın.
- İç içe geçmeyi azaltmak için erken dön.

### Kod Organizasyonu
- İlgili işlevselliği bir araya getir.
- Tutarlı dosya yapısı kullan.
- Endişeleri modüllere/sınıflara ayır.
- Dosyaları odaklı ve makul boyutta tut.
- Net klasör hiyerarşileri kullan.

### Hata Önleme
- Sınırlarda girdileri doğrula.
- Mümkün olduğunda tip sistemlerini kullan.
- Uç durumları açıkça ele al.
- Net mesajlarla hızlı başarısızlık uygula.
- Savunmacı programlama tekniklerini kullan.

### Kod Okunabilirliği
- İnsanların okuması için kod yaz.
- Tutarlı biçimlendirme kullan.
- Görsel ayırma için boşluk ekle.
- Satır uzunluğunu sınırla (80-120 karakter).
- Anlamlı değişken isimleri kullan.

### DRY Prensibi
- Kendini Tekrar Etme (Don't Repeat Yourself).
- Ortak işlevselliği çıkar.
- Çoğaltma yerine yapılandırma kullan.
- Yeniden kullanılabilir bileşenler oluştur.
- DRY'yi netlikle dengele.

### SOLID Prensipleri
- **Tek Sorumluluk**: Değişmek için tek bir neden.
- **Açık/Kapalı**: Genişletmeye açık, değiştirmeye kapalı.
- **Liskov Yerine Geçme**: Alt tipler değiştirilebilir olmalı.
- **Arayüz Ayrımı**: Birçok özel arayüz.
- **Bağımlılık Tersine Çevirme**: Soyutlamalara bağımlı ol.

### En 0yi Uygulamalar
- Kalıtım yerine kompozisyonu tercih et.
- Kodun için testler yaz.
- Düzenli olarak refaktör yap.
- Sürüm kontrolünü etkili kullan.
- Mimari kararları belgele.
- Güvenlik açıklarına karşı kodu kontrol et (örn. SQL enjeksiyonu, XSS).
- Performans için kritik bölümleri optimize et.
- Kod gözden geçirme sürecinde yapıcı ve detaylı geri bildirimler ver.
- Uzun kod geliştirmelerinde ADE'de kilitlenme problemini yaşamamak için kodları parçalı olarak oluşturup son kod paketinden sonra birleştir.

### Parçalı Kod Geliştirme
Uzun kod geliştirme süreçlerinde ADE'de yaşanabilecek kilitlenme problemlerini önlemek için aşağıdaki adımları izleyin:

1. Kodunuzu mantıksal bölümlere ayırın.
2. Her bölümü ayrı ayrı geliştirin ve test edin.
3. Parçaları geliştirirken araç kontrollerini sık sık yapın.
4. Her parçayı tamamladığınızda, ADE'ye gönderin ve onay alın.
5. Tüm parçalar tamamlandığında, son bir paket halinde birleştirin.
6. Birleştirilmiş kodu test edin ve gerekirse son düzeltmeleri yapın.

Bu yaklaşım, hem kilitlenme riskini azaltır hem de daha modüler ve yönetilebilir bir kod geliştirme süreci sağlar.

## 2. Dokümantasyon ve Kullanıcı Arayüzü Metinleri

### Dokümantasyon İlkeleri
- Her API endpoint'i için açık ve kapsamlı dokümantasyon sağla.
- Karmaşık kod bloklarını açıklayan yorumlar ekle.
- README dosyasında projenin amacını, kurulum adımlarını ve kullanım örneklerini belirt.
- Her sürüm için anlamlı bir değişiklik günlüğü (CHANGELOG) tut.
- Dökümantasyonu güncel tut, kod değişikliklerini yansıt.

### Metin Yazma Kuralları
- Net ve öz ol. Gereksiz kelimelerden kaçın.
- Pazarlama diline ve gereksiz süslü ifadelere yer verme.
- Eylem odaklı dil kullan, kullanıcının ne yapması gerektiğine odaklan.
- Tutarlı biçimlendirme ve terminoloji kullan.
- Teknik detaylar hakkında kesin ol.
- Gereksiz bilgi tekrarından kaçın.
- Düğme ve eylem metinlerini net yaz.
- Profesyonel ve tarafsız bir ton kullan.
- Kullanıcı sorularını öngör ve yanıtla.
- Kullanıcı arayüzü metinlerinin entegre hissettir.

### Metin Yazımında Dikkat Edilecek Noktalar
- Belirsiz zaman ifadelerinden kaçın, kesin ol.
- Kullanıcı odaklı dil kullan.
- Ön bilgi varsaymaktan kaçın, gerektiğinde kısaca açıkla veya dokümantasyona bağlantı ver.
- Pozitif dil kullanmayı tercih et.
- Kritik eylemlerde dikkat dağıtıcı unsurları minimize et.
- Hata mesajlarını kullanıcıya rehberlik edecek şekilde yaz.
- Onay mesajlarını net ve güven verici yaz.

### Arayüz Metin Kuralları
- Form etiketlerini ve girişlerini basit tut.
- Tüm Çağrı Düğmelerini (CTA) spesifik yap.
- Kısa ama anlaşılır ol.
- Netliği zekice görünmeye tercih et.
- Göster, anlatma.
- Düğmeler ve bağlantılar dışında her yerde cümle yapısı kullan.
- Hata mesajlarını yardımcı ve sakin bir şekilde yaz.
- Karmaşık bilgileri aşamalı olarak göster.
- Pasif yapıdan kaçın, aktif yapı kullan.
- Arayüz metin tutarlılığını koru.
- Gereksiz açıklamalardan kaçın, kullanıcının ne yaptığını bildiğini varsay.

Örnek:
```markdown
Kötü: "Cluster'iniz mümkün olan en kısa sürede başlayacaktır."
İyi: "Anında başlat"

Kötü: "GPU'ların gücünü açığa çıkarın."
İyi: "H100 GPU cluster'i dağıt"

Kötü: "Cluster kurulumunuz tamamlandı ve artık kullanmaya başlayabilirsiniz."
İyi: "Cluster'iniz hazır."
```

Bu kuralları uygulayarak, dokümantasyon ve kullanıcı arayüzü metinlerinizi daha etkili, anlaşılır ve kullanıcı dostu hale getirebilirsiniz.

## 3. Hata Yönetimi ve Test

### Hata Yönetimi Prensipleri
- Hızlı ve net bir şekilde başarısız ol.
- Eyleme geçirilebilir hata mesajları sağla.
- Hataları uygun bağlamla birlikte logla.
- Hataları doğru seviyede ele al.
- Hataları asla sessizce yutma.

### Hata Türleri ve Yönetimi
- Özel hata türleri tanımla ve kullan.
- Hata türlerine göre farklı işlemler yap.
- Bağlam bilgisiyle birlikte logla.
- Beklenmeyen hataları sar ve anlaşılır mesajlar döndür.

Örnek (TypeScript):
```typescript
class ValidationError extends Error {
    constructor(message: string, public field?: string) {
        super(message);
        this.name = 'ValidationError';
    }
}

async function fetchUserData(userId: string): Promise<User> {
    try {
        // ... (veri çekme işlemleri)
    } catch (error) {
        logger.error('Failed to fetch user data', {
            userId,
            error: error instanceof Error ? error.message : 'Unknown error',
            stack: error instanceof Error ? error.stack : undefined,
        });
        
        if (error instanceof ValidationError) {
            throw error; // Validation hatalarını çağıranın ele almasına izin ver
        }
        
        // Beklenmeyen hataları sar
        throw new Error('Unable to retrieve user data. Please try again later.');
    }
}
```

### Hata Kurtarma Stratejileri
- Yeniden deneme mantığı uygula.
- Devre kesici deseni kullan.
- Zarif bir şekilde bozulma stratejileri uygula.

### En İyi Uygulamalar
- try-catch-finally bloklarını uygun şekilde kullan.
- UI bileşenlerinde hata sınırları oluştur.
- Global hata işleyicileri uygula.
- Erken doğrulama yap ve hızlı başarısız ol.
- Kullanıcı dostu hata mesajları sağla.
- Hataları yeterli bağlamla birlikte logla.
- Hata kalıplarını izle ve uyarı ver.
- Hata senaryolarını açıkça test et.

### Test
- Her yeni özellik veya hata düzeltmesi için birim testleri yaz.
- Entegrasyon testleri ile bileşenlerin birlikte çalışmasını doğrula.
- Uçtan uca testler ile kullanıcı senaryolarını simüle et.
- Test verilerini üretim verilerinden ayır ve güvenli şekilde yönet.
- TDD yaklaşımını benimse: önce testi yaz, sonra kodu geliştir.
- Test kapsamını düzenli olarak kontrol et ve artır.
- Hata senaryoları için özel testler yaz.

## 4. Bulut Mimarileri, DevOps ve Dağıtım

### Bulut-Native Uygulamalar
- Mikroservis mimarisini benimseyin.
- Stateless uygulamalar tasarlayın.
- Konfigürasyon yönetimi için ortam değişkenlerini ve konfigürasyon servislerini kullanın.
- Event-driven mimariler ve pub/sub modellerini kullanın.

### Containerization
- Docker kullanarak uygulamalarınızı containerize edin.
- Multi-stage builds kullanarak container boyutunu optimize edin.
- Container güvenliği için en iyi uygulamaları takip edin (minimal base image, non-root user, etc.).

Örnek (Dockerfile):
```dockerfile
# Build stage
FROM node:14 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:14-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm ci --only=production
USER node
CMD ["node", "dist/main.js"]
```

### Kubernetes
- Deployment, Service, ve Ingress kaynaklarını kullanarak uygulamalarınızı orkestre edin.
- Resource requests ve limits belirleyin.
- Horizontal Pod Autoscaler kullanarak otomatik ölçeklendirme yapın.
- ConfigMaps ve Secrets kullanarak konfigürasyon yönetimi yapın.

Örnek (Kubernetes Deployment):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:1.0.0
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        ports:
        - containerPort: 8080
```

### Bulut Sağlayıcılarının Özel Servisleri

#### AWS
- EC2 veya ECS yerine AWS Fargate kullanarak sunucusuz container çalıştırma.
- S3 ve CloudFront kullanarak statik içerik dağıtımı.
- RDS veya Aurora kullanarak yönetilen veritabanları.

#### Azure
- Azure Kubernetes Service (AKS) ile yönetilen Kubernetes.
- Azure Functions ile sunucusuz işlevler.
- Azure Cosmos DB ile global ölçekli NoSQL veritabanı.

#### GCP
- Google Kubernetes Engine (GKE) ile yönetilen Kubernetes.
- Cloud Run ile sunucusuz container çalıştırma.
- BigQuery ile büyük veri analitiği.

#### Firebase
- Realtime Database veya Firestore ile gerçek zamanlı veri senkronizasyonu.
- Firebase Authentication ile kullanıcı kimlik doğrulama.
- Cloud Functions for Firebase ile sunucusuz backend.

#### Supabase
- Postgres veritabanı ile güçlü veri depolama.
- Realtime subscriptions ile gerçek zamanlı güncellemeler.
- Edge Functions ile sunucusuz işlevler.

### CI/CD Pipeline
- Açıklayıcı iş akışı (workflow) ve görev (job) isimleri kullan.
- İş akışlarını amaca göre düzenle (ci.yml, deploy.yml, release.yml).
- Görev bağımlılıklarını 'needs' ile düzgün bir şekilde uygula.
- Çoklu sürüm testleri için matris yapıları kullan.
- Yeniden kullanılabilir iş akışları ile tekrarı azalt (DRY prensibi).

### Güvenlik En İyi Uygulamaları
- Hassas veriler için bulut sağlayıcılarının secret management servislerini kullanın (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager).
- GITHUB_TOKEN izinleri için en az ayrıcalık prensibini uygula.
- Action sürümlerini belirli commit'lere veya tag'lere sabitle.
- Bulut sağlayıcı kimlik doğrulaması için OIDC kullan.
- Bağımlılıklardaki güvenlik açıklarını tara.

### Performans Optimizasyonu
- Bağımlılıkları uygun şekilde önbelleğe al (npm, pip, vb.).
- Görevler arasında artifact'leri verimli kullan.
- Bağımsız görevleri paralelleştir.
- Gereksiz çalışmaları önlemek için koşullu iş akışları uygula.
- Eski çalışmaları iptal etmek için eşzamanlılık grupları kullan.

### Hata Yönetimi
- Uygun zaman aşımı değerleri belirle.
- Tutarsız adımlar için yeniden deneme mantığı ekle.
- Stratejik olarak 'continue-on-error' kullan.
- Bilgilendirici hata mesajları oluştur.
- Kritik hatalar için bildirimler ayarla.

### Genel En İyi Uygulamalar
- Tekrarlanan görevler için bileşik (composite) action'lar kullan.
- İş akışlarını yorumlarla belgelendirin.
- Dal koruma kuralları uygula.
- Dağıtım aşamaları için ortamlar (environments) kullan.
- İş akışı metriklerini ve maliyetlerini izle.

### Altyapı Yönetimi
- Infrastructure as Code (IaC) prensibini benimseyin.
- Terraform veya bulut sağlayıcıya özgü IaC araçlarını kullanın (AWS CloudFormation, Azure Resource Manager, Google Cloud Deployment Manager).
- Loglama ve izleme araçlarını entegre et (örn. ELK stack, Prometheus, Grafana).
- Düzenli yedekleme ve felaket kurtarma planları oluştur.

Örnek (Terraform ile AWS Altyapı Tanımı):
```hcl
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorld"
  }
}

resource "aws_s3_bucket" "static_website" {
  bucket = "my-static-website-bucket"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}
```

Bu kuralları ve örnekleri uygulayarak, bulut-native uygulamalar geliştirebilir, DevOps süreçlerinizi optimize edebilir ve dağıtım süreçlerinizi daha güvenli, verimli ve ölçeklenebilir hale getirebilirsiniz. Her zaman projenizin özel gereksinimlerini göz önünde bulundurarak bu prensipleri uygulayın ve gerektiğinde uyarlayın.

## 5. Güvenlik ve DevSecOps

### Güvenlik Prensipleri
- Kullanıcı girişine asla güvenme.
- Derinlemesine savunma uygula.
- Güvenli bir şekilde başarısız ol.
- En az yetki prensibini kullan.
- Güvenliği basit tut.
- Güvenlik sorunlarını doğru bir şekilde düzelt.

### OWASP Top 10 Güvenlik Riskleri ve Önlemleri

1. **Broken Access Control**
   - Rol tabanlı erişim kontrolü (RBAC) uygula.
   - Her isteğin yetkilendirmesini kontrol et.
   - Varsayılan olarak erişimi reddet.

   Örnek (Node.js/Express):
   ```javascript
   function checkRole(role) {
     return (req, res, next) => {
       if (req.user && req.user.role === role) {
         next();
       } else {
         res.status(403).json({ error: 'Unauthorized' });
       }
     }
   }

   app.get('/admin', checkRole('admin'), (req, res) => {
     // Admin işlemleri
   });
   ```

2. **Cryptographic Failures**
   - Güçlü şifreleme algoritmaları kullan (AES, RSA, elliptic curve).
   - Hassas verileri her zaman şifrelenmiş olarak sakla.
   - Güvenli anahtar yönetimi uygula.

   Örnek (Python):
   ```python
   from cryptography.fernet import Fernet

   def encrypt_data(data):
       key = Fernet.generate_key()
       f = Fernet(key)
       encrypted_data = f.encrypt(data.encode())
       return key, encrypted_data

   def decrypt_data(key, encrypted_data):
       f = Fernet(key)
       decrypted_data = f.decrypt(encrypted_data).decode()
       return decrypted_data
   ```

3. **Injection**
   - Parametreli sorgular kullan.
   - Girdi doğrulama ve temizleme yap.
   - ORM kullan.

   Örnek (Java/JDBC):
   ```java
   String query = "SELECT * FROM users WHERE username = ? AND password = ?";
   PreparedStatement pstmt = connection.prepareStatement(query);
   pstmt.setString(1, username);
   pstmt.setString(2, password);
   ResultSet rs = pstmt.executeQuery();
   ```

4. **Insecure Design**
   - Tehdit modelleme yap.
   - Güvenli tasarım prensiplerini uygula.
   - Düzenli güvenlik incelemeleri yap.

5. **Security Misconfiguration**
   - Tüm ortamlar için güvenli yapılandırma kılavuzları oluştur.
   - Otomatik yapılandırma doğrulama araçları kullan.
   - Gereksiz özellikleri ve bileşenleri kaldır.

6. **Vulnerable and Outdated Components**
   - Düzenli olarak bağımlılıkları güncelle.
   - Güvenlik açıklarını otomatik olarak kontrol et.
   - Güvenli kaynakları kullan.

   Örnek (npm için):
   ```bash
   npm audit
   npm update
   ```

7. **Identification and Authentication Failures**
   - Güçlü parola politikaları uygula.
   - Çok faktörlü kimlik doğrulama kullan.
   - Oturum yönetimini güvenli hale getir.

   Örnek (Python/Django):
   ```python
   from django.contrib.auth.decorators import login_required
   from django.contrib.auth.mixins import UserPassesTestMixin

   @login_required
   def profile_view(request):
       # Profil görüntüleme işlemleri

   class AdminView(UserPassesTestMixin, View):
       def test_func(self):
           return self.request.user.is_staff
   ```

8. **Software and Data Integrity Failures**
   - Güvenilir kaynakları kullan.
   - Bileşenlerin bütünlüğünü doğrula.
   - CI/CD pipeline'larını güvenli hale getir.

9. **Security Logging and Monitoring Failures**
   - Tüm güvenlik olaylarını logla.
   - Merkezi log yönetimi uygula.
   - Anormal davranışları tespit etmek için log analizi yap.

   Örnek (Python):
   ```python
   import logging

   logging.basicConfig(filename='security.log', level=logging.INFO,
                       format='%(asctime)s:%(levelname)s:%(message)s')

   def log_security_event(event_type, details):
       logging.info(f"Security Event: {event_type} - {details}")
   ```

10. **Server-Side Request Forgery (SSRF)**
    - Beyaz liste kullanarak izin verilen URL'leri sınırla.
    - Gelen istekleri doğrula ve filtrele.
    - Ağ erişimini sınırla.

### Güvenlik Testleri
- Otomatik güvenlik taramaları yap (SAST, DAST, SCA).
- Düzenli penetrasyon testleri yap.
- Güvenlik açığı ödül programları uygula.
- Fuzzing testleri yap.

Örnek (OWASP ZAP ile otomatik tarama):
```bash
zap-cli quick-scan --self-contained --start-options '-config api.disablekey=true' https://example.com
```

### DevSecOps Prensipleri
1. **Güvenliği En Baştan Entegre Et**
   - Güvenliği SDLC'nin her aşamasına dahil et.
   - Güvenlik gereksinimlerini proje başlangıcında belirle.

2. **Sürekli Güvenlik Testleri**
   - CI/CD pipeline'larına güvenlik testlerini entegre et.
   - Her kod değişikliğinde otomatik güvenlik kontrolleri yap.

3. **Güvenlik Otomasyonu**
   - Güvenlik kontrolleri ve düzeltmelerini otomatikleştir.
   - Güvenlik yapılandırmalarını kod olarak yönet (Security as Code).

4. **Güvenlik Eğitimi ve Kültürü**
   - Tüm ekip üyelerine düzenli güvenlik eğitimleri ver.
   - Güvenlik bilincini artır ve güvenli kodlama alışkanlıklarını teşvik et.

5. **Tehdit Modelleme**
   - Düzenli tehdit modelleme oturumları yap.
   - Potansiyel tehditleri ve risklerini belirle ve önlemler al.

6. **Hızlı Geri Bildirim Döngüleri**
   - Güvenlik bulgularını hızlı bir şekilde raporla ve düzelt.
   - Güvenlik metriklerini izle ve sürekli iyileştir.

7. **Üçüncü Parti Güvenliği**
   - Tüm üçüncü parti bileşenleri ve servislerinin güvenliğini kontrol et.
   - Güvenlik gereksinimleri sözleşmelere dahil et.

### En İyi Uygulamalar
- Gizli bilgileri asla kodda saklama, çevresel değişkenler veya güvenli anahtar yönetim sistemleri kullan.
- HTTPS kullan ve güçlü şifreleme algoritmalarını tercih et.
- Düzenli güvenlik taramaları ve penetrasyon testleri yap.
- Hız sınırlama uygula.
- Güvenlik olaylarını logla ve analiz et.
- Bağımlılıkları güncel tut ve güvenlik yamalarını hızlıca uygula.
- Statik ve dinamik analiz araçlarını kullan.
- Güvenlik odaklı kod incelemeleri yap.
- Yaygın güvenlik açıkları için sürekli test yap.
- Güvenlik olay müdahale planı oluştur ve düzenli olarak test et.

Bu kapsamlı güvenlik yaklaşımını uygulayarak, uygulamalarınızın ve sistemlerinizin güvenliğini önemli ölçüde artırabilir, potansiyel tehditlere karşı daha iyi hazırlanabilir ve güvenlik risklerini minimize edebilirsiniz. Güvenlik, sürekli bir süreçtir ve bu prensiplerin düzenli olarak gözden geçirilmesi ve güncellenmesi önemlidir.

## 6. API Tasarımı

API tasarımı, modern uygulama geliştirmenin kritik bir parçasıdır. Projenizin gereksinimlerine bağlı olarak farklı API türleri arasında seçim yapabilirsiniz. Aşağıda, üç popüler API türü için tasarım prensipleri ve örnekler bulunmaktadır.

### RESTful API

RESTful API'ler, kaynak odaklı ve durumsuz yapıları yla HTTP protokolünü kullanarak veri alışverişi yapar.

#### Temel Prensipler:
1. Kaynak odaklı URL'ler kullan
2. HTTP metotlarını (GET, POST, PUT, DELETE) doğru şekilde uygula
3. Uygun HTTP durum kodlarını kullan
4. Hiyerarşik yapıyı URL'lerde yansıt
5. Versiyonlama uygula

#### Örnek:
```
GET /api/v1/users           # Tüm kullanıcıları listele
GET /api/v1/users/123       # ID'si 123 olan kullanıcıyı getir
POST /api/v1/users          # Yeni kullanıcı oluştur
PUT /api/v1/users/123       # ID'si 123 olan kullanıcıyı güncelle
DELETE /api/v1/users/123    # ID'si 123 olan kullanıcıyı sil
```

#### Ne Zaman Kullanmalı:
- CRUD operasyonları ağırlıklı uygulamalarda
- Geniş ekosistem ve araç desteği gerektiğinde
- Basit ve anlaşılır bir API yapısı istendiğinde

### GraphQL

GraphQL, istemcilerin tam olarak ihtiyaç duydukları verileri sorgulamalarına olanak tanıyan bir API sorgulama dili ve çalışma zamanıdır.

#### Temel Prensipler:
1. Tek bir endpoint kullan
2. İstemci tarafından yönlendirilen sorgular oluştur
3. Güçlü tip sistemi kullan
4. İlişkisel verileri etkili bir şekilde sorgula
5. Resolver fonksiyonları ile veri kaynağından bağımsız ol

#### Örnek:
```graphql
type Query {
  user(id: ID!): User
  posts(userId: ID!): [Post]
}

type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post]
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

# Sorgu örneği
query {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}
```

#### Ne Zaman Kullanmalı:
- Karmaşık, iç içe geçmiş veri yapıları olan uygulamalarda
- Mobil uygulamalar gibi bant genişliğinin önemli olduğu durumlarda
- Hızlı prototipleme ve frontend geliştirme gerektiğinde

### gRPC

gRPC, Google tarafından geliştirilen, yüksek performanslı ve düşük gecikmeli bir RPC (Remote Procedure Call) çerçevesidir.

#### Temel Prensipler:
1. Protocol Buffers kullanarak veri seri hale getirme
2. HTTP/2 üzerine inşa edilmiş bi-directional streaming
3. Güçlü tip güvenliği sağlama
4. Kod üretme ile hızlı geliştirme
5. Çoklu dil desteği

#### Örnek (Protocol Buffers):
```protobuf
syntax = "proto3";

service UserService {
  rpc GetUser (UserRequest) returns (User) {}
  rpc ListUsers (UserListRequest) returns (stream User) {}
}

message UserRequest {
  string user_id = 1;
}

message UserListRequest {
  int32 page_size = 1;
  string page_token = 2;
}

message User {
  string user_id = 1;
  string name = 2;
  string email = 3;
}
```

#### Ne Zaman Kullanmalı:
- Mikroservis mimarileri için
- Yüksek performans ve düşük gecikme gerektiğinde
- Servisler arası iletişimde, özellikle iç sistemlerde
- Gerçek zamanlı streaming uygulamalarında

### API Seçimi ve Tasarım Süreci

1. **Proje Gereksinimlerini Analiz Et**
   - Veri yapısı karmaşıklığı
   - Performans ihtiyaçları
   - İstemci çeşitliliği (web, mobil, IoT vb.)
   - Ölçeklenebilirlik gereksinimleri

2. **Kullanım Senaryolarını Belirle**
   - CRUD operasyonları
   - Gerçek zamanlı güncellemeler
   - Toplu veri işlemleri

3. **API Türünü Seç**
   - RESTful API, GraphQL veya gRPC arasında seçim yap
   - Gerekirse hibrit bir yaklaşım kullan (Ör. REST + GraphQL)

4. **API Tasarımını Yap**
   - Endpoint'leri veya şemayı tasarla
   - Veri modellerini oluştur
   - Güvenlik önlemlerini planla

5. **Dokümantasyon Oluştur**
   - API referans dokümanları hazırla (Ör. Swagger, GraphQL Playground)
   - Kullanım örnekleri ve entegrasyon kılavuzları yaz

6. **Test ve İterasyon**
   - Unit ve entegrasyon testleri yaz
   - Performans testleri yap
   - Gerektiğinde tasarımı revize et

7. **Versiyonlama ve Bakım Stratejisi Belirle**
   - API versiyonlama yaklaşımını seç (URL, header, vb.)
   - Geriye dönük uyumluluk politikası oluştur
   - API yaşam döngüsü yönetimi planla

Bu yaklaşımı kullanarak, projenizin ihtiyaçlarına en uygun API türünü seçebilir ve etkili bir API tasarımı gerçekleştirebilirsiniz. Her API türünün kendi güçlü yönleri ve kullanım senaryoları vardır, bu nedenle projenizin gereksinimlerini dikkatli bir şekilde değerlendirmek önemlidir.

## 7. Modern Frontend Frameworks

Modern web uygulaması geliştirmede, frontend framework'leri kritik bir rol oynar. Bu bölümde, popüler frontend framework'lerini ve bunların en iyi uygulamalarını inceleyeceğiz.

### Genel En İyi Uygulamalar

1. **Component-Based Architecture**: Yeniden kullanılabilir, modüler bileşenler oluşturun.
2. **State Management**: Uygulamanın durumunu etkili bir şekilde yönetin.
3. **Performance Optimization**: Hızlı yükleme ve sorunsuz kullanıcı deneyimi sağlayın.
4. **Responsive Design**: Farklı cihazlarda tutarlı bir görünüm elde edin.
5. **Accessibility (a11y)**: Herkes için erişilebilir uygulamalar oluşturun.
6. **Testing**: Unit, integration ve end-to-end testleri yazın.
7. **Code Splitting**: Uygulamanızı daha küçük parçalara bölerek performansı artırın.

### React

#### Component Architecture
- Functional componentleri ve hooks'ları tercih edin.
- Props drilling'den kaçının, context veya state management çözümleri kullanın.
- Higher-Order Components (HOC) ve Render Props desenlerini uygun şekilde kullanın.

#### State Management
- Küçük uygulamalar için: React Context + useReducer
- Orta-büyük ölçekli uygulamalar için: Redux (Redux Toolkit ile) veya MobX
- Server state için: React Query veya SWR

#### Performance Optimization
- `React.memo`, `useMemo`, ve `useCallback` hooks'larını kullanın.
- Virtüalizasyon tekniklerini uygulayın (react-window veya react-virtualized).
- Lazy loading ve Suspense kullanarak kod bölme yapın.

Örnek (Performance Optimization):
```jsx
import React, { useMemo, useCallback } from 'react';

const ExpensiveComponent = React.memo(({ data, onItemClick }) => {
  // Component logic
});

const ParentComponent = ({ items }) => {
  const memoizedData = useMemo(() => expensiveCalculation(items), [items]);
  
  const handleItemClick = useCallback((id) => {
    console.log('Item clicked:', id);
  }, []);

  return <ExpensiveComponent data={memoizedData} onItemClick={handleItemClick} />;
};
```

### Vue.js

#### Component Architecture
- Single-File Components (SFC) kullanın.
- Props ve emits ile parent-child iletişimini sağlayın.
- Mixins yerine Composition API kullanın (Vue 3).

#### State Management
- Küçük uygulamalar için: Vue's Reactive API
- Büyük uygulamalar için: Vuex veya Pinia

#### Performance Optimization
- `v-once` ve `v-memo` direktiflerini kullanın.
- Async components ve dynamic imports ile kod bölme yapın.
- Keep-alive component'i ile component önbellekleme yapın.

Örnek (Composition API ile State Management):
```vue
<script setup>
import { ref, computed } from 'vue';

const count = ref(0);
const doubleCount = computed(() => count.value * 2);

function increment() {
  count.value++;
}
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
  <p>Double count is: {{ doubleCount }}</p>
</template>
```

### Angular

#### Component Architecture
- Smart (container) ve Presentational (dumb) component'leri ayırın.
- OnPush change detection strategy'yi kullanın.
- Dependency Injection'ı etkili bir şekilde kullanın.

#### State Management
- Küçük-orta ölçekli uygulamalar için: Services ve RxJS
- Büyük uygulamalar için: NgRx (Redux pattern)

#### Performance Optimization
- Lazy loading modules kullanın.
- Pure pipes kullanarak hesaplamaları optimize edin.
- TrackBy fonksiyonu ile ngFor performansını artırın.

Örnek (OnPush Strategy ve Async Pipe):
```typescript
import { Component, ChangeDetectionStrategy } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-user-list',
  template: `
    <ul>
      <li *ngFor="let user of users$ | async; trackBy: trackByFn">{{ user.name }}</li>
    </ul>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserListComponent {
  users$: Observable<User[]>;

  trackByFn(index: number, user: User): string {
    return user.id;
  }
}
```

### Svelte

#### Component Architecture
- Bileşen tabanlı yapıyı benimseyin.
- Props ve events ile bileşenler arası iletişim kurun.
- Stores ile global state yönetimi yapın.

#### State Management
- Yerel state için reactive declarations kullanın.
- Global state için Svelte stores kullanın.

#### Performance Optimization
- Svelte'in otomatik optimizasyonlarından faydalanın.
- `{#key}` bloklarını kullanarak gereksiz render'ları önleyin.

Örnek (Svelte Store ve Reactive Declarations):
```svelte
<script>
import { writable } from 'svelte/store';

const count = writable(0);
let doubleCount;

$: doubleCount = $count * 2;

function increment() {
  count.update(n => n + 1);
}
</script>

<button on:click={increment}>Count is: {$count}</button>
<p>Double count is: {doubleCount}</p>
```

### Backend Entegrasyonu ve UI Template Kullanımı

1. **API İntegrasyonu**: Backend API'nizi frontend framework'ünüzle entegre edin.
   - RESTful API'ler için: Axios veya Fetch API kullanın.
   - GraphQL için: Apollo Client veya Relay kullanın.

2. **Authentication**: JWT veya OAuth gibi güvenli kimlik doğrulama yöntemlerini uygulayın.

3. **UI Template Entegrasyonu**: 
   - Template'in stil sistemini (CSS, SASS, CSS-in-JS) projenize uyarlayın.
   - Componentleri framework'ünüze uygun şekilde dönüştürün.
   - Tema ve stil değişkenlerini global olarak yönetin.

4. **Responsive Design**: Template'in responsive özelliklerini koruyun ve geliştirin.

5. **Asset Management**: Template'in statik dosyalarını (resimler, fontlar) uygun şekilde yönetin.

6. **Custom Hooks/Composables**: Template fonksiyonlarını framework'ünüze özel hooks veya composable'lara dönüştürün.

Örnek (React ile UI Template Entegrasyonu):
```jsx
// Theme provider
import { ThemeProvider } from 'styled-components';
import theme from './theme';

// Global styles
import { GlobalStyle } from './globalStyles';

// Template component adapted for React
import { Button } from './components/Button';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <div className="app">
        <Button primary>Template Button</Button>
      </div>
    </ThemeProvider>
  );
}
```

Bu yaklaşımları kullanarak, modern frontend framework'lerini etkili bir şekilde kullanabilir, performanslı ve bakımı kolay uygulamalar geliştirebilir, ve UI template'lerinizi sorunsuz bir şekilde entegre edebilirsiniz. Her projenin kendine özgü gereksinimleri olduğunu unutmayın ve bu best practice'leri projenizin ihtiyaçlarına göre uyarlayın.

## 6. Proje Yönetimi

### Görev Yönetimi
- Her görev için açık tanımlar ve kabul kriterleri belirle.
- Ürün Gereksinim Dokümanı (PRD) temel alarak detaylı görev listesi oluştur.
- Görevleri ana görevler ve alt görevler şeklinde hiyerarşik olarak yapılandır.
- Görev listesini Markdown formatında `/tasks/` dizininde sakla.
- İlgili dosyaları ve notları görev listesine ekle.

### Sürüm Kontrolü
- Git için anlamlı commit mesajları yaz.
- Feature branch yaklaşımını kullan.
- Pull request'leri detaylı incelemelerden geçir.
- Dal koruma kuralları uygula.

### Proje Yapısı
- Proje yapısını modüler ve ölçeklenebilir tut.
- Teknik borcu düzenli olarak ele al ve refaktör yap.
- Kod kalitesini korumak için statik kod analiz araçları kullan.

### Metodoloji
- Agile metodolojileri benimse.
- Sprint planlaması yap ve düzenli retrospektifler düzenle.
- Kan-ban tahtaları veya proje yönetim araçları kullan.

### İletişim ve Dokümantasyon
- Proje ilerlemesini düzenli olarak raporla.
- Teknik kararları ve mimarileri belgelendir.
- Ekip içi iletişimi artırmak için düzenli toplantılar yap.

### Kalite Güvencesi
- Otomatik testleri CI/CD pipeline'ına entegre et.
- Kod incelemelerini zorunlu hale getir.
- Performans ve güvenlik testleri yap.

Örnek (Görev Listesi Formatı):
```markdown
## İlgili Dosyalar

- `src/components/UserProfile.tsx` - Kullanıcı profili ana bileşeni.
- `src/components/UserProfile.test.tsx` - UserProfile için birim testleri.
- `src/api/userProfile.ts` - Profil güncelleme API entegrasyonu.
- `src/api/userProfile.test.ts` - API entegrasyonu için testler.

### Notlar

- Birim testleri genellikle test edilen kod dosyalarıyla aynı dizinde bulunmalıdır.
- Testleri çalıştırmak için `npx jest` komutunu kullanın.

## Görevler

- [ ] 1.0 Kullanıcı Profili Düzenleme Arayüzünü Oluştur
  - [ ] 1.1 Profil bilgileri formu komponenti oluştur
  - [ ] 1.2 Form doğrulama mantığını ekle
- [ ] 2.0 Profil Güncelleme API Entegrasyonu
  - [ ] 2.1 API isteği gönderme fonksiyonunu yaz
  - [ ] 2.2 Başarılı/başarısız durumları işle
- [ ] 3.0 Birim Testleri Yaz
```

Bu yaklaşım, projenizi daha iyi yönetmenize, ekip içi iletişimi artırmanıza ve proje kalitesini yükseltmenize yardımcı olacaktır.

## 7. Dil ve Çerçeve Spesifik En İyi Uygulamalar

### Python ve Django
- List comprehension ve generator ifadelerini uygun yerlerde kullan.
- Django'nun yerleşik özelliklerini ve araçlarını mümkün olduğunca kullan.
- PEP 8 uyumluluğunu sağla ve Django'nun kodlama stil kılavuzunu takip et.
- Karmaşık görünümler için Sınıf Tabanlı Görünümler (CBV), basit mantık için Fonksiyon Tabanlı Görünümler (FBV) kullan.
- Django ORM'yi veritabanı etkileşimleri için kullan, performans gerekmedikçe ham SQL sorgularından kaçın.
- MVT (Model-View-Template) desenine sıkı sıkıya bağlı kal.
- Django'nun yerleşik test araçlarını (unittest ve pytest-django) kullan.

### JavaScript/TypeScript
- Asenkron işlemler için async/await kullan.
- Tip güvenliği için TypeScript'i tercih et.
- ESLint ve Prettier gibi araçları kullanarak kod stilini standartlaştır.
- Modül sistemini (ES6 modules) kullanarak kodu organize et.

### Go
- Error handling için if err != nil pattern'ini kullan.
- Arayüzleri (interfaces) etkin bir şekilde kullan.
- Go'nun yerleşik concurrency özelliklerini (goroutines ve channels) uygun şekilde kullan.
- Paket yapısını mantıklı ve organize bir şekilde tasarla.

### React
- Gereksiz render'ları önlemek için useMemo ve useCallback hooks'larını kullan.
- Fonksiyonel bileşenleri ve hooks'ları tercih et.
- Prop drilling'den kaçınmak için Context API veya state yönetim kütüphaneleri kullan.
- Bileşen yapısını mantıklı ve yeniden kullanılabilir şekilde tasarla.

### FastAPI
- Pydantic modellerini kullanarak request ve response şemalarını tanımla.
- Dependency Injection sistemini etkin bir şekilde kullan.
- Asenkron fonksiyonları uygun yerlerde kullan.
- API dokümantasyonunu otomatik olarak oluşturmak için FastAPI'nin OpenAPI özelliklerinden yararlan.

### Genel İlkeler
- Her dil ve çerçeve için resmi dokümantasyonu ve topluluk tarafından kabul görmüş en iyi uygulamaları takip et.
- Kod okunabilirliğini ve bakım yapılabilirliğini önceliğe al.
- Dil ve çerçeve spesifik güvenlik en iyi uygulamalarını uygula.
- Performans optimizasyonlarını düşün, ancak erken optimizasyondan kaçın.
- Sürüm kontrolü ve paket yönetimi için dile özgü standart araçları kullan.

Her dil ve çerçeve için spesifik kurallar ve en iyi uygulamalar daha detaylı olabilir. Projenizin ihtiyaçlarına ve kullandığınız teknolojilere göre bu kuralları genişletebilir ve özelleştirebilirsiniz.

## 8. Performans ve Ölçeklenebilirlik

### Performans Prensipleri
- Optimize etmeden önce ölçüm yap.
- Önce kritik yolu optimize et.
- Algoritmik karmaşıklığı dikkate al.
- Performans ile okunabilirlik arasında denge kur.
- Maliyetli işlemleri önbelleğe al.

### Algoritmik Optimizasyon
- Zaman karmaşıklığının farkında ol ve daha verimli algoritmalar kullan.
- Uygun veri yapılarını seç (Map, Set, vs.).

### Bellek Optimizasyonu
- Nesne havuzlama tekniklerini kullan.
- Bellek verimli desenler uygula (generators, vs.).

### Asenkron Performans
- Paralel işleme ve eşzamanlı programlama tekniklerini kullan.
- Kontrollü eşzamanlılık uygula.

### Veritabanı Optimizasyonu
- Veritabanı sorgularını optimize et, gerekli indeksleri oluştur.
- N+1 sorgu probleminden kaçın, ilişkili verileri tek sorguda çek.
- Bağlantı havuzlama (connection pooling) kullan.

### Önbellekleme Stratejileri
- Çok seviyeli önbellekleme uygula (in-memory, distributed cache).
- Caching mekanizmalarını (Redis, Memcached) etkin kullan.
- LRU (Least Recently Used) gibi önbellek yenileme stratejileri uygula.

### Sistem Ölçeklenebilirliği
- Asenkron işlemler ve kuyruk sistemleri (RabbitMQ, Kafka) ile arka plan görevlerini yönet.
- Yük dengeleme ve otomatik ölçeklendirme stratejileri uygula.
- Mikroservis mimarisi kullanarak sistem bileşenlerini bağımsız olarak ölçeklendir.

### İçerik Dağıtımı
- CDN kullanarak statik içeriklerin dağıtımını optimize et.
- Lazy loading tekniklerini uygula.

### En İyi Uygulamalar
- Optimize etmeden önce profilleme yap.
- Uygun veri yapılarını kullan.
- Bellek tahsislerini minimize et.
- Mümkün olduğunda işlemleri toplu halde gerçekleştir.
- Stratejik olarak önbellekleme uygula.
- Performans metriklerini izle.
- Gecikmeli yükleme (ör. lazy loading) kullan.
- Önce kritik yolları optimize et.

Örnek (Paralel İşleme):
```javascript
async function fetchMultipleUrls(urls) {
    // İyi: Paralel işleme
    const results = await Promise.all(
        urls.map(url => fetch(url))
    );
    
    // Daha İyi: Kontrollü eşzamanlılık
    const concurrencyLimit = 5;
    const results = [];
    for (let i = 0; i < urls.length; i += concurrencyLimit) {
        const batch = urls.slice(i, i + concurrencyLimit);
        const batchResults = await Promise.all(
            batch.map(url => fetch(url))
        );
        results.push(...batchResults);
    }
    
    return results;
}
```

Bu kuralları uygulayarak, uygulamanızın performansını artırabilir ve daha iyi ölçeklenebilirlik sağlayabilirsiniz.

## 9. Kodun Yeniden Kullanılabilirliği ve Bakımı

### SOLID Prensipleri

#### Single Responsibility Principle (SRP)
- Her sınıf veya fonksiyonun tek bir sorumluluğu ve değişmek için tek bir nedeni olmalı.
- Farklı endüşeler (UI, iş mantığı, veri erişimi) doğru şekilde ayrılmalı.

#### Open/Closed Principle (OCP)
- Kod, genişletmeye açık ama değiştirmeye kapalı olmalı.
- Soyutlamalar, arayüzler veya kalıtımı etkili bir şekilde kullan.
- Genişletme noktalarını iyi tanımla ve belgelendir.

#### Liskov Substitution Principle (LSP)
- Alt tipler, program doğruluğunu etkilemeden temel tiplerin yerine geçebilmeli.
- Türetilmiş sınıflar, temel sınıfların kullanıldığı her yerde kullanılabilmeli.
- Geçersiz kılınan metodlar aynı davranış garantilerini korumalı.

#### Interface Segregation Principle (ISP)
- Arayüzler istemciye özel olmalı, genel amaçlı olmamalı.
- Arayüzler odaklı ve minimal olmalı.
- Şişman arayüzleri daha küçük parçalara böl.

#### Dependency Inversion Principle (DIP)
- Yüksek seviyeli modüller, somut uygulamalar yerine soyutlamalara bağımlı olmalı.
- Bağımlılık enjeksiyonu veya kontrol tersine çevirmeyi etkili bir şekilde kullan.
- Bağımlılıklar açık olmalı, gizli olmamalı.

### Yeniden Kullanılabilirlik
- Tekrar eden kod bloklarını fonksiyonlara veya sınıflara ayır.
- Dependency Injection pattern'ini kullan, bağımlılıkları azalt.
- Sık kullanılan işlevler için utility sınıfları veya modülleri oluştur.
- Kod parçalarını modüller halinde organize et.

### Bakım
- Legacy kodu kademeli olarak refaktör et, büyük değişiklikler yerine küçük iyileştirmeler yap.
- Kod dokumantasyonunu güncel tut.
- Düzenli kod incelemeleri yap.
- Teknik borçları takip et ve zamanında öde.

Örnek (Single Responsibility Principle):
```python
# Kötü: Birden fazla sorumluluğu olan sınıf
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save(self):
        # Kullanıcıyı veritabanına kaydet
        pass
    
    def send_email(self, message):
        # Kullanıcıya e-posta gönder
        pass

# İyi: Sorumlulukları ayrılmış
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        # Kullanıcıyı veritabanına kaydet
        pass

class EmailService:
    def send_email(self, user, message):
        # Kullanıcıya e-posta gönder
        pass
```

Bu kuralları uygulayarak, kodunuzun yeniden kullanılabilirliğini artırabilir ve bakımını kolaylaştırabilirsiniz.

## 10. Sürekli İyileştirme ve Gözlemlenebilirlik

### Kod Kalitesi ve Analiz
- Kod kalitesi metriklerini (cyclomatic complexity, maintainability index) düzenli olarak ölç.
- Statik kod analiz araçlarını (SonarQube, ESLint) kullan ve uyarıları gider.
- Performans profillemesi yap ve darboğazları tespit et.
- Düzenli kod incelemeleri yap ve en iyi uygulamaları paylaş.

### Loglama En İyi Uygulamaları
- Yapılandırılmış loglama kullan (JSON formatı).
- İstek izleme için korelasyon ID'leri ekle.
- Uygun seviyelerde logla (ERROR, WARN, INFO, DEBUG).
- Hassas bilgileri loglamaktan kaçın.
- Log toplama ve merkezileştirme uygula.

### Metrik Uygulaması
- Dört Altın Sinyal'i takip et (gecikme, trafik, hatalar, doygunluk).
- Standart metrik adlandırma kurallarını kullan.
- Özel iş metrikleri uygula.
- Anlamlı gösterge panoları oluştur.
- SLI'lar, SLO'lar ve hata bütçeleri tanımla.

### Dağıtık İzleme
- Satıcıdan bağımsız izleme için OpenTelemetry uygula.
- Kritik işlemler için span'lar ekle.
- Span özniteliklerine ilgili bağlamı dahil et.
- Performans için izleri uygun şekilde örnekle.
- İzleri loglar ve metriklerle ilişkilendir.

### Uyarı Stratejisi
- Nedenlere değil, belirtilere göre uyarı ver.
- Net eskalasyon politikaları belirle.
- Uygun eşiklerle uyarı yorgunluğundan kaçın.
- Uyarı açıklamalarına runbook'ları dahil et.
- Uyarıları düzenli olarak test et.

### Performans İzleme
- Uygulama performans metriklerini (APM) izle.
- Veritabanı sorgu performansını takip et.
- Gerçek kullanıcı izleme (RUM) uygula.
- Üçüncü taraf servis bağımlılıklarını izle.
- Kritik yollar için sentetik izleme kur.

### Geliştirme Süreci İyileştirmeleri
- Kullanıcı geri bildirimlerini topla ve ürün geliştirme sürecine dahil et.
- Düzenli olarak yeni teknolojileri ve en iyi uygulamaları araştır, uygun olanları entegre et.
- Sürekli entegrasyon ve sürekli dağıtım (CI/CD) süreçlerini optimize et.
- Teknik borçları düzenli olarak ele al ve refaktöring yap.

### En İyi Uygulamalar
- Gözlemlenebilirliği başlangıçtan itibaren uygula.
- Metrikler, loglar ve izler arasında tutarlı adlandırma kullan.
- Gözlemlenebilirlik stratejinizi belgele.
- Gösterge panolarını düzenli olarak gözden geçir ve güncelle.
- Olay müdahale prosedürlerini uygula ve pratik yap.

Örnek (Yapılandırılmış Loglama):
```javascript
// İyi: Bağlamlı yapılandırılmış loglama
logger.info({
  event: 'user_login',
  userId: user.id,
  correlationId: req.correlationId,
  duration: Date.now() - startTime,
  metadata: {
    ipAddress: req.ip,
    userAgent: req.headers['user-agent']
  }
});

// İyi: Etiketli metrik
metrics.increment('api_requests_total', {
  method: req.method,
  endpoint: req.route.path,
  status: res.statusCode
});
```

Bu uygulamaları takip ederek, kodunuzun ve sistemlerinizin kalitesini sürekli olarak iyileştirebilir, performansını artırabilir ve sorunları daha hızlı tespit edip çözebilirsiniz.

## 11. UI/UX Tasarımı ve Geliştirme

### Odak Alanları
- React bileşen mimarisi (hook'lar, context, performans)
- Tailwind/CSS-in-JS ile responsive CSS
- Durum yönetimi (Redux, Zustand, Context API)
- Frontend performansı (lazy loading, kod bölme, memoization)
- Erişilebilirlik (WCAG uyumluluğu, ARIA etiketleri, klavye navigasyonu)

### Yaklaşım
1. Bileşen odaklı düşünme - yeniden kullanılabilir, bileşilebilir UI parçaları
2. Mobil öncelikli responsive tasarım
3. Performans bütçeleri - 3 saniyenin altında yüklenme süreleri hedefle
4. Semantik HTML ve uygun ARIA öznitelikleri
5. Uygun olduğunda TypeScript ile tip güvenliği

### Tasarım Prensipleri
- Tutarlı bir tasarım sistemi oluştur ve uygula (renk paleti, tipografi, bileşenler).
- Responsive tasarım prensiplerini uygula, farklı cihaz ve ekran boyutlarına uyum sağla.
- Erişilebilirlik standartlarına (WCAG) uy, ekran okuyucu uyumluluğunu sağla.
- Kullanıcı merkezli tasarım yaklaşımını benimse, kullanıcı araştırmaları ve testleri yap.
- Micro-interactions ve animasyonları ölçülü ve anlamlı bir şekilde kullan.
- Design system dokümantasyonu oluştur ve güncel tut.
- Dark mode ve tema desteği için esnek CSS yapısı kur.

### Bileşen Mimarisi (React örneği)
- TypeScript arayüzleri ile fonksiyon bileşenlerini yaz.
- Açıklayıcı bileşen ve prop isimleri kullan.
- Başarısız olabilecek bileşenler için uygun hata sınırları uygula.
- Bileşenleri varsayılan (default) export olarak dışa aktar.
- Durum yönetimi ve yan etkiler için React hook'larını kullan.
- Kolaylıkla test edilebilen bileşenler yaz.

### Durum Yönetimi
- Yerel bileşen durumu için useState kullan.
- Karmaşık durum mantığı için useReducer kullan.
- Bileşenler arası durum paylaşımı için Context API'yi kullan.
- Büyük uygulamalar için durum yönetimi kütüphanelerini (Redux, Zustand) düşün.
- Durumu mümkün olduğunca ihtiyaç duyulduğu yere yakın tut.

### Performans Optimizasyonu
- Maliyetli bileşenler için React.memo kullan.
- useMemo ve useCallback'i uygun şekilde uygula.
- Büyük bileşenler için lazy loading ve kod bölme (code splitting) tekniklerini kullan.
- Bağımlılıkları doğru yöneterek gereksiz yeniden render'ları önle.
- Performans darboğazlarını belirlemek için React DevTools Profiler'i kullan.
- 3 saniyenin altında yüklenme süresi hedefle.

### Bileşen Desenleri
- İlişkili UI elemanları için bileşik bileşenler kullan.
- Esnek bileşen API'leri için render props uygula.
- Bileşen mantığını çıkarmak ve yeniden kullanmak için özel hook'lar kullan.
- Uygun olduğunda container/presentational bileşen desenini takip et.
- Bileşenleri tek bir sorumluluğa odaklı tut.

### Kullanıcı Deneyimi İyileştirme
- A/B testleri yaparak kullanıcı deneyimini sürekli iyileştir.
- Hata mesajları ve kullanıcı bilgilendirmelerini açık ve yardımcı olacak şekilde tasarla.
- Sayfa yükleme sürelerini optimize et ve kullanıcıya geri bildirim sağla.
- Kullanıcı geri bildirimlerini topla ve analiz et, UI/UX iyileştirmeleri için kullan.

### En İyi Uygulamalar
- Sınıf bileşenlerini mutlaka gerekli olmadıkça kullanma.
- Uygun TypeScript tiplemeleri olmadan bileşen yazma.
- 300 satırdan fazla kodu olan bileşenler oluşturma.
- Prop'lar için any veya unknown tiplerini kullanma.
- Asenkron işlemler için hata yönetimini atlama.
- Semantik HTML kullan ve uygun ARIA özniteliklerini ekle.
- Klavye navigasyonunu destekle.

### Çıktı
- Props arayüzü ile tam bir React bileşeni
- Stil çözümü (Tailwind sınıfları veya styled-components)
- Gerektiğinde durum yönetimi uygulaması
- Temel birim test yapısı
- Bileşen için erişilebilirlik kontrol listesi
- Performans düşünceleri ve optimizasyonlar

Örnek (React Bileşeni):
```typescript
// UserProfile.tsx
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import styled from 'styled-components';

interface UserData {
  id: string;
  name: string;
  email: string;
  role: string;
}

interface UserProfileProps {
  userId: string;
  onUpdate: (userData: UserData) => void;
}

// Styled components
const ProfileContainer = styled.div`
  padding: 1rem;
  background-color: #f0f0f0;
  border-radius: 8px;
  max-width: 400px;
  margin: 0 auto;
`;

const ProfileHeader = styled.h2`
  color: #333;
  font-size: 1.5rem;
  margin-bottom: 1rem;
`;

const ProfileInfo = styled.p`
  color: #666;
  margin-bottom: 0.5rem;
`;

const UpdateButton = styled.button`
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: #0056b3;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.5);
  }
`;

const ErrorMessage = styled.div`
  color: #dc3545;
  margin-top: 1rem;
`;

const LoadingSpinner = styled.div`
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
  margin: 20px auto;

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;

const UserProfile: React.FC<UserProfileProps> = ({ userId, onUpdate }) => {
  const [userData, setUserData] = useState<UserData | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Memoized function to fetch user data
  const fetchUserData = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(`/api/users/${userId}`);
      if (!response.ok) throw new Error('Failed to fetch user data');
      const data = await response.json();
      setUserData(data);
    } catch (err) {
      setError('An error occurred while fetching user data');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }, [userId]);

  useEffect(() => {
    fetchUserData();
  }, [fetchUserData]);

  // Memoized update handler
  const handleUpdate = useCallback(() => {
    if (userData) {
      onUpdate(userData);
    }
  }, [userData, onUpdate]);

  // Memoized user role
  const userRole = useMemo(() => {
    return userData?.role.charAt(0).toUpperCase() + userData?.role.slice(1);
  }, [userData]);

  if (isLoading) return <LoadingSpinner aria-label="Loading user data" />;
  if (error) return <ErrorMessage role="alert">{error}</ErrorMessage>;
  if (!userData) return null;

  return (
    <ProfileContainer>
      <ProfileHeader>{userData.name}'s Profile</ProfileHeader>
      <ProfileInfo>Email: {userData.email}</ProfileInfo>
      <ProfileInfo>Role: {userRole}</ProfileInfo>
      <UpdateButton onClick={handleUpdate} aria-label="Update user profile">
        Update Profile
      </UpdateButton>
    </ProfileContainer>
  );
};

export default UserProfile;

// Usage example:
// <UserProfile userId="123" onUpdate={(userData) => console.log('Updated:', userData)} />
```

Bu örnek, aşağıdaki özellikleri göstermektedir:
- TypeScript ile tip güvenliği
- React hooks (useState, useEffect, useCallback, useMemo)
- Styled-components ile stil uygulama
- Performans optimizasyonları (useCallback, useMemo)
- Erişilebilirlik özellikleri (ARIA etiketleri)
- Hata yönetimi ve yükleme durumları
- Responsive tasarım için hazır yapı

Bu kuralları ve örneği uygulayarak, kullanıcı dostu, performanslı ve bakımı kolay UI/UX tasarımları ve uygulamaları geliştirebilirsiniz.

Bu kurallar, ADE'nin kod kalitesini, güvenliğini, performansını ve kullanıcı deneyimini artırmak için kullanılabilir. Her projenin özel ihtiyaçlarına göre bu kurallar uyarlanabilir ve genişletilebilir.

## 12. Backend Mimarisi

### Odak Alanları
- RESTful API tasarımı (uygun versiyonlama ve hata yönetimi ile)
- Servis sınırlarının tanımlanması ve servisler arası iletişim
- Veritabanı şema tasarımı (normalizasyon, indeksler, sharding)
- Önbellekleme stratejileri ve performans optimizasyonu
- Temel güvenlik kalıpları (kimlik doğrulama, hız sınırlama)

### Yaklaşım
1. Net servis sınırları ile başla
2. API'leri sözleşme öncelikli tasarla
3. Veri tutarlılığı gereksinimlerini dikkate al
4. Başlangıçtan itibaren yatay ölçeklenebilirlik için plan yap
5. Basit tut - erken optimizasyondan kaçın

### RESTful API Tasarımı
- Uygun HTTP metotlarını kullan (GET, POST, PUT, DELETE, vb.)
- Tutarlı ve anlaşılır endpoint isimlendirmesi yap
- API versiyonlamasını uygula (URL veya header-based)
- Hata kodları ve mesajları için standart bir format belirle
- Sayfalama, filtreleme ve sıralama için querystring parametrelerini kullan

Örnek (API Endpoint Tanımı):
```yaml
POST /api/v1/users
Description: Yeni bir kullanıcı oluşturur
Request Body:
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
Response:
  201 Created:
    {
      "id": "uuid",
      "username": "string",
      "email": "string",
      "createdAt": "timestamp"
    }
  400 Bad Request:
    {
      "error": "string",
      "details": ["string"]
    }
```

### Servis Mimarisi
- Mikroservis veya monolitik mimari arasında bilinçli seçim yap
- Servisler arası iletişim için uygun protokolleri seç (HTTP, gRPC, mesaj kuyrukları)
- Servis discovery ve yük dengeleme mekanizmaları uygula
- Hata toleransı ve dayaniklilik için circuit breaker pattern'ini kullan
- Distributed tracing için unique request ID'leri kullan

Servis Mimarisi Örneği (ASCII Diagram):
```
+------------+     +-------------+     +--------------+
|            |     |             |     |              |
|   User     |     |   Product   |     |    Order     |
|  Service   |     |   Service   |     |   Service    |
|            |     |             |     |              |
+------------+     +-------------+     +--------------+
       |                  |                   |
       |                  |                   |
       v                  v                   v
+---------------------------------------------+
|                                             |
|              API Gateway                    |
|                                             |
+---------------------------------------------+
                    |
                    |
                    v
        +------------------------+
        |                        |
        |      Load Balancer     |
        |                        |
        +------------------------+
                    |
                    |
                    v
        +------------------------+
        |                        |
        |       Client Apps      |
        |                        |
        +------------------------+
```

### Veritabanı Tasarımı
- Uygun veritabanı türünü seç (relational, NoSQL, NewSQL)
- Veritabanı şemalarını normalize et ve gerektiğinde denormalize et
- Performans için uygun indeksleri oluştur
- Büyük veri setleri için sharding stratejileri uygula
- Veritabanı bağlantılarını havuzla (connection pooling)

Veritabanı Şema Örneği:
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
```

### Performans Optimizasyonu
- Önbellekleme stratejileri uygula (Redis, Memcached)
- Asenkron işleme ve mesaj kuyrukları kullan
- Veritabanı sorgularını optimize et
- CDN kullanımını değerlendir
- Lazy loading ve pagination tekniklerini uygula

### Güvenlik
- Güçlü kimlik doğrulama ve yetkilendirme mekanizmaları uygula
- HTTPS kullan ve SSL/TLS sertifikalarını güncel tut
- Input validation ve sanitization uygula
- Rate limiting ve throttling mekanizmaları ekle
- Güvenlik açıkları için düzenli taramalar yap

### Çıktı
- API endpoint tanımları (örnek istek ve yanıtlarla)
- Servis mimarisi diyagramı (mermaid veya ASCII)
- Anahtar ilişkileri içeren veritabanı şeması
- Kısa gerekçelerle teknoloji önerileri listesi
- Potansiyel darboğazlar ve ölçeklendirme önlemleri

Bu kuralları uygulayarak, sağlam, ölçeklenebilir ve güvenli backend mimarileri tasarlayabilir ve uygulayabilirsiniz. Her zaman somut örnekler sağlamaya ve teoriden ziyade pratik uygulamaya odaklanmaya özen gösterin.

## 13. Microservices Mimarisi

### Servis Sınırlarını Belirleme
- Her servisin tek bir iş sorumluluğu olmasını sağlayın (Single Responsibility Principle).
- Domain-Driven Design (DDD) prensiplerini kullanarak bounded context'leri belirleyin.
- Servislerin birbirinden bağımsız olarak geliştirilebilir, test edilebilir ve deploy edilebilir olmasını sağlayın.

### Servisler Arası İletişim
- Senkron iletişim için REST veya gRPC kullanın.
- Asenkron iletişim için mesaj kuyrukları (RabbitMQ, Apache Kafka) kullanın.
- API Gateway pattern'ini uygulayarak istemci-servis iletişimini yönetin.

Örnek (gRPC Servis Tanımı):
```protobuf
syntax = "proto3";

package userservice;

service UserService {
  rpc GetUser (GetUserRequest) returns (User) {}
  rpc CreateUser (CreateUserRequest) returns (User) {}
  rpc UpdateUser (UpdateUserRequest) returns (User) {}
  rpc DeleteUser (DeleteUserRequest) returns (DeleteUserResponse) {}
}

message GetUserRequest {
  string user_id = 1;
}

message User {
  string user_id = 1;
  string name = 2;
  string email = 3;
}

// Diğer mesaj tanımları...
```

### Veri Tutarlılığı Stratejileri
- Eventual Consistency modelini benimseyin.
- Saga pattern'ini kullanarak dağıtık işlemleri yönetin.
- CQRS (Command Query Responsibility Segregation) pattern'ini kullanarak okuma ve yazma işlemlerini ayırın.

### Distributed Tracing
- Her isteğe benzersiz bir correlation ID atayın.
- OpenTelemetry gibi araçları kullanarak distributed tracing uygulayın.
- Logging ve monitoring stratejinizi microservices mimarisine uygun şekilde tasarlayın.

Örnek (Distributed Tracing - Python):
```python
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

resource = Resource(attributes={SERVICE_NAME: "user-service"})

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("get_user"):
    # İş mantığı
    user = get_user_from_database(user_id)
    with tracer.start_as_current_span("process_user_data"):
        # Kullanıcı verilerini işle
        processed_user = process_user(user)
```

### Ölçeklenebilirlik ve Dayanıklılık
- Her servisi bağımsız olarak ölçeklendirilebilir şekilde tasarlayın.
- Circuit Breaker pattern'ini uygulayarak servis hatalarını izole edin.
- Health check endpoint'leri ekleyerek servis sağlığını izleyin.

### En İyi Uygulamalar
- Microservices için standart bir template veya boilerplate oluşturun.
- Servislerin bağımsız olarak deploy edilebilmesi için CI/CD pipeline'larını ayarlayın.
- Service discovery ve load balancing için Kubernetes veya benzeri orkestrasyon araçları kullanın.
- API versiyonlama stratejisi belirleyin ve uygulayın.
- Düzenli olarak servis bağımlılıklarını gözden geçirin ve gerektiğinde refaktör edin.

Bu yaklaşımları uygulayarak, ölçeklenebilir, dayanıklı ve bakımı kolay microservices mimarileri oluşturabilirsiniz. Her zaman projenizin özel gereksinimlerini göz önünde bulundurarak bu prensipleri uygulayın ve gerektiğinde uyarlayın.

## 13. Kod İncelemesi (Code Review)

### Yaklaşım
1. git diff komutunu çalıştırarak son değişiklikleri gör
2. Değiştirilmiş dosyalara odaklan
3. İncelemeye hemen başla

### İnceleme Kontrol Listesi
- Kod basit ve okunabilir mi?
- Fonksiyonlar ve değişkenler iyi isimlendirilmiş mi?
- Tekrar eden kod var mı?
- Uygun hata yönetimi uygulanmış mı?
- Gizli bilgiler veya API anahtarları açığa çıkarılmış mı?
- Girdi doğrulaması uygulanmış mı?
- İyi test kapsamı var mı?
- Performans düşünceleri ele alınmış mı?

### Geri Bildirim Organizasyonu
Geri bildirimleri öncelik sırasına göre organize edin:
1. Kritik sorunlar (mutlaka düzeltilmeli)
2. Uyarılar (düzeltilmesi önerilir)
3. Öneriler (iyileştirme için düşünülebilir)

### En İyi Uygulamalar
- Her zaman yapıcı ve saygılı ol
- Sorunların nasıl düzeltileceğine dair spesifik örnekler ver
- Olumlu yönleri de vurgula
- Büyük resmi göz önünde bulundur
- Kod stil kılavuzlarına atıfta bulun
- Gerektiğinde yüz yüze tartışmayı öner

Örnek (Kod İncelemesi Geri Bildirimi):
```markdown
### Kritik Sorunlar
1. `processUserData` fonksiyonunda kullanıcı girdisi doğrulanmamış. Lütfen XSS ve enjeksiyon saldırılarını önlemek için girdi doğrulaması ekleyin.
   Örnek: `sanitizeInput(userData.name)` gibi bir fonksiyon kullanabilirsiniz.

### Uyarılar
1. `fetchData` fonksiyonu hata yönetimi eksik. Try-catch bloğu ekleyerek hata durumlarını ele alın.
2. `UserComponent` 200 satırdan fazla, daha küçük bileşenlere bölmeyi düşünün.

### Öneriler
1. `calculateTotal` fonksiyonuna JSDoc yorum eklemek, kullanımını daha açık hale getirebilir.
2. Performans için `useMemo` hook'unu kullanmayı düşünebilirsiniz.

### Olumlu Noktalar
- Temiz ve tutarlı kod stili, okuması kolay.
- Fonksiyon ve değişken isimlendirmeleri açıklayıcı.
- Test kapsamı iyi düşünülmüş.
```

Bu yaklaşımı uygulayarak, daha etkili ve verimli kod incelemeleri yapabilir, ekip içi işbirliğini geliştirebilir ve kod kalitenizi sürekli olarak iyileştirebilirsiniz.

## 14. Hata Ayıklama (Debugging)

### Başlangıç Adımları
1. Hata mesajını ve yığın izini (stack trace) yakala
2. Yeniden üretme adımlarını belirle
3. Hatanın gerçekleştiği yeri izole et
4. Minimal düzeltme uygula
5. Çözümün çalıştığını doğrula

### Hata Ayıklama Süreci
- Hata mesajlarını ve logları analiz et
- Son kod değişikliklerini kontrol et
- Hipotezler oluştur ve test et
- Stratejik hata ayıklama logları ekle
- Değişken durumlarını incele

### Raporlama
Her sorun için aşağıdakileri sağlayın:
- Kök neden açıklaması
- Teşhisi destekleyen kanıtlar
- Spesifik kod düzeltmesi
- Test yaklaşımı
- Önleme önerileri

### En İyi Uygulamalar
- Sistematik bir yaklaşım benimse
- Varsayımları doğrula, gerçeklere dayan
- Basit ve izole edilmiş test senaryoları oluştur
- Hata ayıklama araçlarını etkili bir şekilde kullan (breakpoint'ler, adım adım yürütme)
- İşbirliği yap, gerektiğinde yardım iste

Örnek (Hata Ayıklama Raporu):
```markdown
### Sorun Açıklaması
Kullanıcılar, profil resimlerini güncellerken "500 Internal Server Error" alıyor.

### Kök Neden
Dosya yükleme işlemi sırasında, sistem geçici dosya dizininin yazılabilir izinleri eksik.

### Kanıtlar
1. Sunucu loglarında şu hata mesajı görülüyor: "PermissionError: [Errno 13] Permission denied: '/tmp/uploads/'"
2. Hata, yalnızca profil resmi güncelleme işlemlerinde gerçekleşiyor.
3. Dizin izinlerini kontrol ettiğimizde, '/tmp/uploads/' dizininin yazma izinlerinin eksik olduğu görüldü.

### Düzeltme
```python
import os

# Uygulama başlatma sırasında çalıştırılacak
upload_dir = '/tmp/uploads/'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir, mode=0o755)
else:
    os.chmod(upload_dir, 0o755)
```

### Test Yaklaşımı
1. Farklı boyutlarda profil resimleri yükleyerek manuel testler yapın.
2. Otomatik testlere dosya yükleme senaryoları ekleyin.
3. Sunucu yeniden başlatıldıktan sonra izinlerin korunduğunu doğrulayın.

### Önleme Önerileri
1. Uygulama başlatma sırasında tüm gerekli dizinlerin var olduğunu ve doğru izinlere sahip olduğunu kontrol eden bir script ekleyin.
2. Dosya işlemleri için bir hata işleme katmanı oluşturun ve kullanıcılara daha açıklayıcı hata mesajları gösterin.
3. Dosya yükleme işlemleri için kapsamlı logging ekleyin.
```

Bu yaklaşımı uygulayarak, hata ayıklama sürecinizi daha sistematik ve etkili hale getirebilir, sorunları daha hızlı çözebilir ve benzer hataların gelecekte tekrarlanmasını önleyebilirsiniz.

## 15. Etik ve Sorumluluk

Yazılım geliştirme sürecinde etik ve sosyal sorumluluk konuları, günümüzde giderek daha fazla önem kazanmaktadır. Bu bölümde, etik yazılım geliştirme, veri gizliliği, algoritmik bias ve sürdürülebilir yazılım geliştirme konularında en iyi uygulamaları ele alacağız.

### Etik Yazılım Geliştirme

1. **Şeffaflık**: Kullanıcılara sistemin nasıl çalıştığı ve kararların nasıl alındığı konusunda açık olun.
2. **Adil Kullanım**: Sistemin tüm kullanıcılara eşit ve adil davranmasını sağlayın.
3. **Zarar Vermeme**: Geliştirdiğiniz sistemin potansiyel zararlarını değerlendirin ve minimize edin.
4. **Kullanıcı Onayı**: Kullanıcıların verilerinin nasıl kullanılacağı konusunda bilgilendirilmiş onayını alın.
5. **Hesap Verebilirlik**: Sistemin kararları ve sonuçları için sorumluluk alın.

Örnek (Etik Karar Alma Süreci):
```python
def ethical_decision(action, impact_assessment):
    if impact_assessment['harm'] > impact_assessment['benefit']:
        return False
    if not impact_assessment['user_consent']:
        return False
    if not impact_assessment['explainable']:
        return False
    return True

# Kullanım
action = "user_data_collection"
impact = {
    'harm': 2,
    'benefit': 8,
    'user_consent': True,
    'explainable': True
}

if ethical_decision(action, impact):
    print("Action is ethical, proceed.")
else:
    print("Action is not ethical, reconsider.")
```

### Veri Gizliliği

1. **Minimizasyon**: Sadece gerekli olan verileri toplayın ve işleyin.
2. **Şifreleme**: Hassas verileri hem iletişim sırasında hem de depolamada şifreleyin.
3. **Anonim Hale Getirme**: Mümkün olduğunda verileri anonim hale getirin.
4. **Erişim Kontrolü**: Verilere erişimi sıkı bir şekilde kontrol edin ve loglayın.
5. **Veri Saklama Politikası**: Net bir veri saklama ve silme politikası oluşturun.

Örnek (Veri Anonim Hale Getirme):
```python
import hashlib

def anonymize_data(user_data):
    anonymized = user_data.copy()
    anonymized['id'] = hashlib.sha256(user_data['id'].encode()).hexdigest()
    anonymized['name'] = 'REDACTED'
    anonymized['email'] = f"{hashlib.md5(user_data['email'].encode()).hexdigest()}@example.com"
    return anonymized

# Kullanım
user = {
    'id': '12345',
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

anonymized_user = anonymize_data(user)
print(anonymized_user)
```

### Algoritmik Bias

1. **Veri Çeşitliliği**: Eğitim verilerinizin çeşitli ve temsili olduğundan emin olun.
2. **Düzenli Denetim**: Algoritmanızın çıktılarını düzenli olarak bias açısından denetleyin.
3. **Çeşitlilik Odaklı Ekip**: Farklı bakış açılarını temsil eden çeşitli bir geliştirme ekibi oluşturun.
4. **Bias Azaltma Teknikleri**: Veri ön işleme ve model tasarımında bias azaltma tekniklerini kullanın.
5. **İnsan Gözetimi**: Kritik kararlarda insan gözetimi ve müdahalesi için mekanizmalar oluşturun.

Örnek (Basit Bias Kontrolü):
```python
def check_gender_bias(model_predictions, actual_outcomes, gender_data):
    male_accuracy = sum([p == a for p, a, g in zip(model_predictions, actual_outcomes, gender_data) if g == 'male']) / gender_data.count('male')
    female_accuracy = sum([p == a for p, a, g in zip(model_predictions, actual_outcomes, gender_data) if g == 'female']) / gender_data.count('female')
    
    bias = abs(male_accuracy - female_accuracy)
    return bias < 0.05  # 5% tolerans

# Kullanım
predictions = [1, 0, 1, 1, 0, 1, 0, 0]
actuals = [1, 0, 1, 1, 1, 1, 0, 0]
genders = ['male', 'female', 'male', 'female', 'female', 'male', 'female', 'male']

if check_gender_bias(predictions, actuals, genders):
    print("No significant gender bias detected.")
else:
    print("Potential gender bias detected. Further investigation needed.")
```

### Sürdürülebilir Yazılım Geliştirme

1. **Enerji Verimliliği**: Yazılımın enerji tüketimini optimize edin.
2. **Kaynak Optimizasyonu**: Sunucu ve depolama kaynaklarını verimli kullanın.
3. **Yeşil Hosting**: Yenilenebilir enerji kullanan hosting sağlayıcıları tercih edin.
4. **Uzun Ömürlü Tasarım**: Yazılımı uzun vadeli kullanım için tasarlayın, sık sık yeniden yazılmasını önleyin.
5. **E-Atık Yönetimi**: Yazılımın donanım gereksinimlerini optimize ederek e-atık oluşumunu azaltın.

Örnek (Enerji Verimliliği Kontrolü):
```python
import time
import psutil

def measure_energy_usage(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_energy = psutil.cpu_percent(interval=None)
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_energy = psutil.cpu_percent(interval=None)
        
        duration = end_time - start_time
        energy_usage = end_energy - start_energy
        
        print(f"Function {func.__name__} took {duration:.2f} seconds and used {energy_usage:.2f}% CPU.")
        return result
    return wrapper

# Kullanım
@measure_energy_usage
def some_heavy_computation():
    # Ağır hesaplama simülasyonu
    for _ in range(10000000):
        pass

some_heavy_computation()
```

### Genel İlkeler

1. **Eğitim ve Farkındalık**: Ekibinizi etik ve sorumluluk konularında düzenli olarak eğitin.
2. **Etik Komitesi**: Önemli kararlar için bir etik komitesi oluşturun.
3. **Açık Kaynak Desteği**: Mümkün olduğunda açık kaynak projelerine katkıda bulunun.
4. **Topluluk Katılımı**: Kullanıcı topluluğunuzla akti f iletişim kurun ve geri bildirimlerini dikkate alın.
5. **Sürekli Değerlendirme**: Etik ve sorumluluk uygulamalarınızı düzenli olarak gözden geçirin ve güncelleyin.

Bu ilkeleri ve uygulamaları benimseyerek, etik, sorumlu ve sürdürülebilir yazılım geliştirme süreçleri oluşturabilirsiniz. Bu yaklaşım, sadece daha iyi yazılımlar üretmenize değil, aynı zamanda topluma ve çevreye olumlu katkıda bulunmanıza da yardımcı olacaktır. Unutmayın ki etik ve sorumluluk, sürekli evrim geçiren konulardır ve bu alandaki gelişmeleri takip etmek önemlidir.