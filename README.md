Learning python and how to structure python packages.

As a package it doesn't work yet but the code and tests can be run from the waterInfrastructure/src dir.


For the given dataset here is the result.
`>>> import waterInfrastructure as wi`
`>>> wi.calculate("https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json")`


result:
``` bash
{'number_water_points': {'Kpatarigu': 51, 'Zuedema': 18, 'Nawaasa': 6, 'Gbima': 3, 'Chondema': 4, 'Luisa': 8, 'Kpikpaluk': 3, 'Namgurima': 8, 'Kanbangsa': 8, 'Zanwara': 10, 'Bechinsa': 26, 'Logvasgsa': 4, 'Nyankpiensa': 8, 'Abanyeri': 4, 'Zangu-Vuga': 13, 'Akpari-yeri': 3, 'Jagsa': 38, 'Dorinsa': 17, 'Nabulugu': 31, 'Jaata': 8, 'Kom': 6, 'Badomsa': 27, 'Jiningsa-Yipaala': 3, 'Tantala': 22, 'Soo': 7, 'Zundem': 30, 'Dibisi': 2, 'Selinvoya': 13, 'Zua': 28, 'Chansa': 9, 'Alavanyo': 3, 'Gbaarigu': 5, 'Fiisa': 5, 'Kurugu': 9, 'Suik': 1, 'Mwalorinsa': 8, 'Tuisa': 4, 'Jiriwiensa': 8, 'Tankangsa': 6, 'Jiniensa': 1, 'Loagri_1_': 18, 'Jiningsa': 7, 'Bandem': 7, 'Nyandema': 3, 'Zogsa': 6, 'Kunkwah': 3, 'Gumaryili': 1, 'Arigu': 12, 'Kaasa': 25, 'Nayoku': 35, 'Vundema': 5, 'Guuta-Nasa': 11, 'Kanwaasa': 9, 'Banyangsa': 10, 'Longsa': 9, 'Garigu': 1, 'Kubore': 18, 'Kalaasa': 1, 'Chanpolinsa': 4, 'Kulbugu': 11, 'Piisa': 5, 'Sikabsa': 3, 'Zukpeni': 6, 'Gaadem': 2, 'Guuta': 32},

'number_functional': 623,

'community_ranking': {'Jiriwiensa': 0.0, 'Kpatarigu': 9.803921568627452, 'Jiniensa': 0.0, 'Zuedema': 0.0, 'Nawaasa': 0.0, 'Gbima': 33.33333333333333, 'Loagri_1_': 22.22222222222222, 'Kubore': 27.77777777777778, 'Chondema': 0.0, 'Jiningsa': 0.0, 'Bandem': 42.857142857142854, 'Luisa': 0.0, 'Nyandema': 0.0, 'Kpikpaluk': 0.0, 'Zogsa': 16.666666666666664, 'Namgurima': 50.0, 'Kanbangsa': 0.0, 'Zanwara': 40.0, 'Kunkwah': 0.0, 'Gumaryili': 0.0, 'Bechinsa': 0.0, 'Nayoku': 17.142857142857142, 'Logvasgsa': 0.0, 'Nyankpiensa': 0.0, 'Abanyeri': 0.0, 'Zangu-Vuga': 15.384615384615385, 'Akpari-yeri': 0.0, 'Jagsa': 15.789473684210526, 'Guuta': 6.25, 'Dorinsa': 5.88235294117647, 'Nabulugu': 12.903225806451612, 'Jaata': 0.0, 'Kom': 0.0, 'Badomsa': 0.0, 'Jiningsa-Yipaala': 0.0, 'Banyangsa': 30.0, 'Longsa': 22.22222222222222, 'Garigu': 0.0, 'Tankangsa': 0.0, 'Tantala': 27.27272727272727, 'Kurugu': 44.44444444444444, 'Vundema': 0.0, 'Soo': 28.57142857142857, 'Zundem': 0.0, 'Kalaasa': 0.0, 'Chanpolinsa': 25.0, 'Dibisi': 0.0, 'Selinvoya': 7.6923076923076925, 'Zua': 14.285714285714285, 'Chansa': 0.0, 'Arigu': 50.0, 'Alavanyo': 33.33333333333333, 'Kulbugu': 9.090909090909092, 'Guuta-Nasa': 0.0, 'Kanwaasa': 11.11111111111111, 'Gbaarigu': 60.0, 'Fiisa': 0.0, 'Piisa': 0.0, 'Kaasa': 0.0, 'Suik': 0.0, 'Sikabsa': 0.0, 'Zukpeni': 66.66666666666666, 'Gaadem': 0.0, 'Mwalorinsa': 0.0, 'Tuisa': 0.0}}

```

Note: Unlike most python code I am using long names and very descriptive ones.
