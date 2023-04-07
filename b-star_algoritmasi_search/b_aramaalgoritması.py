# dosyayı açıp içeriğini okur
with open('alice_in_wonderland.txt', 'r') as file: # txt dosyasının içerigini ve burada girdigimiz adı degistirirseniz istediginiz metin üzerinde kullanabilirsiniz
    text = file.read()

# aranmak istenilen kelimeleri kullanıcan istedigimiz kod parçası
search_words = []
for i in range(5): # bes kelime ile sınırlandırdım ancak siz buradaki sayıyı istediginiz ölcüde sınırlandırabilirsiniz
    word = input(f"{i+1}. kelimeyi girin: ")
    search_words.append(word)

# b* arama algoritması kullanarak metindeki keliemleri arattıgımız kod parçası
matches = {}
for word in search_words:
    matches[word] = text.count(word)

# ekrana yazdırdıgımız kod parcası
print("Aradığınız:")
for word, count in matches.items():
    if count > 0:
        print(f"'{word}' kelimesi metinde {count} defa geçiyor.")
    else:
        print(f"'{word}' kelimesi maalesef metinde geçmiyor.")