# ADE Kuralları Yapısı İçin İyileştirme Önerileri

Bu öneriler, mevcut "ADE-rules" yapısını bir yapay zeka (ADE) tarafından daha verimli bir şekilde kullanılabilir hale getirmeyi amaçlamaktadır.

## 1. Kural Şiddeti/Önceliği (`severity` veya `priority` alanı)

Her kuralın ne kadar kritik olduğunu belirten bir alan eklenmesi, bir ADE'nin önerilerini önceliklendirmesi için çok önemlidir.

*   **Mevcut Durum:** Kuralların önceliği veya şiddeti açıkça belirtilmemiştir.
*   **Öneri:** `rules.json` manifestine ve her kuralın YAML frontmatter'ına `severity` (şiddet) veya `priority` (öncelik) alanı eklenmelidir.
*   **Değer Örnekleri:** `critical`, `high`, `medium`, `low`, `suggestion`.
*   **Faydası:** Bir ADE, kritik güvenlik açıklarını veya performans sorunlarını ele alan kuralları, stil önerilerine göre daha yüksek öncelikli olarak sunabilir.

## 2. Uygulanabilir Teknolojiler (`applies_to` alanı)

Kuralların hangi programlama dilleri, framework'ler veya teknolojiler için geçerli olduğunu daha açık bir şekilde belirtmek, filtrelemeyi ve bağlamsal uygulamayı iyileştirir. `tags` alanı genel kategorizasyon için iyi olsa da, `applies_to` daha spesifik bir filtreleme sağlar.

*   **Mevcut Durum:** Kuralların uygulanabilirliği genellikle `tags` alanı veya kuralın başlığı/açıklaması ile dolaylı olarak anlaşılır.
*   **Öneri:** `rules.json` manifestine ve her kuralın YAML frontmatter'ına `applies_to` (uygulandığı teknolojiler) alanı (dizi formatında) eklenmelidir.
*   **Değer Örnekleri:** `["python", "django", "javascript", "react", "kubernetes"]`.
*   **Faydası:** Bir ADE, sadece üzerinde çalıştığı teknoloji yığınına (örneğin bir React projesi) özel kuralları kolayca filtreleyebilir.

## 3. Otomasyon Potansiyeli ve Önerilen Araçlar (`automation_potential` ve `suggested_tools` alanları)

Bir kuralın otomatik olarak kontrol edilip edilemeyeceği ve hangi araçlarla (linter, statik analiz, CI/CD) kontrol edilebileceği bilgisi, bir ADE'nin kuralı nasıl uygulayacağını belirlemesi için çok değerlidir.

*   **Mevcut Durum:** Bu bilgi genellikle kuralın `Rationale` veya `Automation Potential` bölümlerinde serbest metin olarak yer alır.
*   **Öneri:** `rules.json` manifestine ve her kuralın YAML frontmatter'ına `automation_potential` (otomasyon potansiyeli) ve `suggested_tools` (önerilen araçlar) alanları eklenmelidir.
*   **Değer Örnekleri:**
    *   `automation_potential`: `["linter", "static-analysis", "runtime-check", "manual-review", "ci-cd-check"]`
    *   `suggested_tools`: `["ESLint", "Prettier", "SonarQube", "pytest", "GitHub Actions"]`
*   **Faydası:** Bir ADE, otomatik olarak düzeltilebilecek kuralları belirleyebilir, geliştiriciye hangi araçları kullanması gerektiğini önerebilir veya CI/CD entegrasyonu için ipuçları verebilir.

## 4. Yapılandırılmış Örnek Kod Blokları (`good_example`, `bad_example` alanları)

Şu anda örnek kodlar Markdown içindeki serbest kod bloklarıdır. Bunların daha yapılandırılmış alanlar olarak tanımlanması, bir ADE'nin bu örnekleri doğrudan kullanmasını veya değiştirmesini kolaylaştırır.

*   **Mevcut Durum:** Örnek kodlar, Markdown dosyasının içinde `Good Practice:` veya `Bad Practice:` başlıkları altında yer alan kod bloklarıdır.
*   **Öneri:** Her kuralın YAML frontmatter'ına veya kural içeriğinde özel olarak etiketlenmiş alanlara `good_example_code` ve `bad_example_code` gibi alanlar eklenmelidir. Bu alanlar, kod dilini de belirten bir yapıya sahip olabilir.
*   **Değer Örnekleri:**
    ```yaml
    good_example:
      language: python
      code: |
        def calculate_discounted_price(price, discount_percentage):
            # ...
    bad_example:
      language: python
      code: |
        def calc(p, d):
            # ...
    ```
*   **Faydası:** Bir ADE, bu örnekleri doğrudan alıp geliştiricinin koduna uygulayabilir, benzer hataları tespit edebilir veya düzeltme önerileri oluştururken referans olarak kullanabilir.

## 5. İlişkili Kurallar (`related_rules` alanı)

Bir kuralın diğer kurallarla olan ilişkisini (örneğin, bir kuralın uygulanmasının başka bir kuralı etkilemesi veya tamamlaması) belirtmek, ADE'nin daha bütünsel öneriler sunmasını sağlar.

*   **Mevcut Durum:** Kurallar arasındaki ilişkiler genellikle metin içinde belirtilir veya hiç belirtilmez.
*   **Öneri:** `rules.json` manifestine ve her kuralın YAML frontmatter'ına `related_rules` (ilişkili kurallar) alanı (dizi formatında, kural ID'lerini içeren) eklenmelidir.
*   **Değer Örnekleri:** `["srp", "ocp"]`
*   **Faydası:** Bir ADE, bir kuralı önerirken, ilgili diğer kuralları da göz önünde bulundurarak daha kapsamlı bir çözüm sunabilir veya çakışan kuralları belirleyebilir.

---