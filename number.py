import phonenumbers
import opencage
import folium

from phonenumbers import geocoder

number = input("Telefon nomer kriting misol(+998992223456):")

pepnum = phonenumbers.parse(number)
loca = geocoder.description_for_number(pepnum, 'en')
print(loca)

from phonenumbers import carrier
servis = phonenumbers.parse(number)
print(carrier.name_for_number(servis, 'en'))

from opencage.geocoder import OpenCageGeocode

key = 'd7a536bbaca44fdb96cf3f2be242ca26'

geocoder = OpenCageGeocode(key)
quw = str(loca)
resu = geocoder.geocode(quw)

lat = resu[0]['geometry']['lat']
lng = resu[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(loca=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popu = loca).add_to(myMap)

myMap.save("myLocation.html")