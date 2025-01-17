#Tensorflow
print("hello")

'''
Artificial Neural Network(ANN) = yapay sinir ağları
perceptron => yapay nöron

*********************************************************************************************************************************
aktivasyon fonksiyonları(Activation functions):
ReLU(Rectified Linear Unit)(Düzeltmeli Doğrusal Ünite):(0ile sonsuz arasında değer alır)(derin öğrenme alanında karşımıza çıkar)
linear function(f(x)=x):(sonsuz değer alabilir fakat non-linear olmaması sebebiyle modellerde sorunlara yol açabibilir.)
sigmoid:(0ile1 arasında)(genelde sınıflandırma(Classification))
tanh funcition:(-1ile1 arasında tanjant fonksiyonu)(negatif değerlerde daha geniş kapsam sağlar)(genelde classification)

*********************************************************************************************************************************
problem type:
1.classification
2.regularization

Regularization(regresyon)
-Regresyon, istatistiksel bir yöntem olup, bir veya daha fazla bağımsız değişken kullanarak bir bağımlı (hedef) değişkeni tahmin etmeyi amaçlar.
-Regresyon, bir veri setindeki ilişkileri modelleyerek, bir değişkenin diğer değişkenlere olan bağımlılığını belirlemeye çalışır.
-Regresyon, genellikle sürekli (sayısal) bir hedef değişkeni tahmin etmek için kullanılır. 
-Bir evin fiyatını tahmin etmek (bağımlı değişken: fiyat, bağımsız değişkenler: evin büyüklüğü, oda sayısı, konum vb.).

*********************************************************************************************************************************
veriyi:2ye bölüp
öğrenme verisi
test verisi
öğrendikten sonra
tahmin

"adam","RMSprop" optimmizasyon
learning rate optimize etmek gerekiyor ne kadar düşük olursa o kadar uzun sürer ama bulur. ne kadar yüksek olursa minimumü kaçırabiliriz.
************************************************************************************************
Screenshot_10.png
mavi ve turuncu veriler var.derin ağımız hangisinin turuncu hangisnin mavi oldugunu anlayabiliyor mu

ratio of training to test data %50
test ve öğrenme verisi oranı

noise:gürültü
veriler içerisinde sıkıntı çıkartan veriler

batch size
veri büyüklüğü


overfitting:
Overfitting (aşırı öğrenme), bir makine öğrenimi modelinin eğitim verilerine çok iyi uyum sağlaması, ancak yeni,
görülmemiş verilerle kötü performans göstermesi durumudur. Bu durum, modelin eğitim verisindeki gürültüyü ve 
ayrıntıları aşırı derecede öğrenmesi sonucu ortaya çıkar.
Yani, model eğitim verilerine fazla odaklanır ve genelleme yapabilme yeteneği zayıflar.







'''