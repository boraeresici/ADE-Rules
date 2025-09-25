# SDD Dokümantasyonu İçin Kural Klasör Yapısı Eklemeleri

Bu doküman, tüm projelerin SDD (Software Design Document) dokümantasyonu ile geldiği varsayımıyla, mevcut kural klasör yapısına eklenmesi gereken başlıkları ve açıklamalarını sunmaktadır. Bu eklemeler, bir ADE'nin tasarım dokümanlarını daha doğru ve temiz bir şekilde anlamasını, oluşturmasını veya doğrulamasını sağlayacaktır.

## 1. `architectural-patterns` (Mimari Desenler ve Kararlar)

Bir SDD'nin en temel bileşenlerinden biri, sistemin genel mimarisini ve seçilen mimari desenleri açıklamasıdır. Bu kategori, bir ADE'nin mimari tasarım kararlarını anlamasına ve uygulamasına yardımcı olacak kuralları içermelidir.

*   **Kategori Amacı:** Sistem mimarisi seçimi, desenlerin uygulanması ve mimari ödünleşimler hakkında rehberlik sağlamak.
*   **Örnek Kurallar:**
    *   `layered-architecture.md`: Katmanlı mimari prensipleri ve uygulama yönergeleri.
    *   `hexagonal-architecture.md`: Altıgen mimari (Ports and Adapters) prensipleri.
    *   `event-driven-architecture.md`: Olay tabanlı mimari tasarım kuralları.
    *   `microkernel-architecture.md`: Mikrokernel (Plug-in) mimarisi.
    *   `architectural-tradeoffs.md`: Mimari kararların ödünleşimlerini (örneğin performans vs. maliyet) belgeleme kuralları.
    *   `design-principles.md`: Genel yazılım tasarım prensipleri (DRY, YAGNI, KISS).

## 2. `data-modeling` (Veri Modelleme ve Veritabanı Tasarımı)

`backend` kategorisi genel veritabanı tasarımını kapsasa da, bir SDD genellikle veri modellerine ve veritabanı şemalarına daha derinlemesine odaklanır. Bu kategori, veri modelleme prensiplerini ve stratejilerini detaylandırabilir.

*   **Kategori Amacı:** Veritabanı şeması tasarımı, veri tutarlılığı ve veri evrimi hakkında rehberlik sağlamak.
*   **Örnek Kurallar:**
    *   `normalization-principles.md`: Veritabanı normalizasyon prensipleri (1NF, 2NF, 3NF, BCNF).
    *   `denormalization-strategies.md`: Performans için denormalizasyon stratejileri ve ne zaman kullanılacağı.
    *   `data-consistency-models.md`: Dağıtık sistemlerde veri tutarlılık modelleri (örneğin eventual consistency).
    *   `schema-evolution.md`: Veritabanı şeması evrimi ve değişiklik yönetimi.
    *   `data-privacy-by-design.md`: Tasarımdan itibaren veri gizliliği prensipleri.

## 3. `system-integration` (Sistem Entegrasyonu ve Birlikte Çalışabilirlik)

Bir SDD, farklı sistemlerin nasıl entegre olacağını detaylandırır. Bu kategori, entegrasyon desenleri, veri değişim formatları ve API sözleşmeleri gibi konuları kapsayabilir.

*   **Kategori Amacı:** Farklı sistemler arasındaki entegrasyon stratejileri ve en iyi uygulamalar hakkında rehberlik sağlamak.
*   **Örnek Kurallar:**
    *   `integration-patterns.md`: Kurumsal entegrasyon desenleri (örneğin Message Bus, API Gateway, Shared Database).
    *   `data-exchange-formats.md`: Veri değişim formatları (JSON, XML, Protocol Buffers) ve kullanım senaryoları.
    *   `api-contract-management.md`: API sözleşmelerinin (OpenAPI/Swagger) yönetimi ve sürdürülmesi.
    *   `interoperability-standards.md`: Birlikte çalışabilirlik standartları ve protokolleri.

## 4. `requirements-traceability` (Gereksinim İzlenebilirliği ve Yönetimi)

Bir SDD, gereksinimlerle doğrudan bağlantılıdır. Bu kategori, gereksinimlerin tasarıma nasıl yansıtıldığını ve değişikliklerin nasıl yönetildiğini gösteren kuralları içerebilir.

*   **Kategori Amacı:** Gereksinimlerden tasarıma izlenebilirliği sağlama ve gereksinim değişikliklerini yönetme.
*   **Örnek Kurallar:**
    *   `requirements-to-design-traceability.md`: Gereksinimlerin tasarım öğeleriyle nasıl ilişkilendirileceği.
    *   `change-impact-analysis.md`: Tasarım değişikliklerinin gereksinimler üzerindeki etkisini analiz etme.
    *   `non-functional-requirements.md`: Fonksiyonel olmayan gereksinimlerin (performans, güvenlik, ölçeklenebilirlik) SDD'ye dahil edilmesi.

## 5. `technology-selection` (Teknoloji Seçimi ve Gerekçelendirme)

SDDD'ler genellikle teknoloji seçimlerini ve bu seçimlerin gerekçelerini içerir. Bu kategori, teknoloji seçim sürecine rehberlik eden kuralları barındırabilir.

*   **Kategori Amacı:** Teknoloji seçimi sürecini standartlaştırmak ve kararların gerekçelerini belgelemek.
*   **Örnek Kurallar:**
    *   `technology-evaluation-criteria.md`: Teknoloji değerlendirme kriterleri (maliyet, topluluk desteği, olgunluk, performans).
    *   `build-vs-buy-analysis.md`: Geliştirme mi, satın alma mı karar analizi.
    *   `technology-stack-consistency.md`: Teknoloji yığını tutarlılığı.
