#!/usr/bin/env python
from mailjet_rest import Client
import os

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

data = {
    'Messages': [
        {
            "From": {
                "Email": "bombaylviv@gmail.com",
                "Name": "Магазин Бомбей"
            },
            "To": [
                {"Email": "yuliia.pryima@gmail.com"},
                {"Email": "pryima@stryi.com.ua"},
            ],
            "Subject": "Оновлення у магазині Бомбей!",
            "HTMLPart": """<div style="background-color: #fff3cd;">
                            <h1 style="text-align: center; font-family: Georgia; padding-top: 20px; color: #793b14;"><em><strong>Доброго дня</strong></em></h1>
                            <p><img src="https://s15.postimg.cc/97qm3tzez/bombay.jpg" alt="bombay" style="display: block; margin-left: auto; margin-right: auto;" width="600" height="800" /></p>
                            <h4 style="text-align: center; font-family: Arial; color: #99823f;"><em>Минулого року Ви здійснювали покупки в нашому інтернет-магазині "Бомбей".</em></h4>
                            <h3 style="text-align: center; font-family: Arial; color: #99823f;">Нещодавно у нас відбулось значне оновлення товару.</h3>
                            <h3 style="text-align: center; font-family: Arial; color: #99823f;">Можливо, Вас зацікавлять нові позиції у таких розділах:</h3>
                            <div></div>
                            <h3 style="text-align: center;"><a href="http://bombayshop.com.ua/vyshyvanki" target="_blank" style="color: #99823f;" data-saferedirecturl="https://www.google.com/url?hl=uk&amp;q=http://bombayshop.com.ua/vyshyvanki&amp;source=gmail&amp;ust=1527766593219000&amp;usg=AFQjCNGmd5mKbN6SP1Gm4-HHlNnNLmn6_A" rel="noopener">Жіночі вишиванки</a></h3>
                            <h3 style="text-align: center;"><a href="http://bombayshop.com.ua/vyshyti_platia" style="color: #99823f;" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=uk&amp;q=http://bombayshop.com.ua/vyshyti_platia&amp;source=gmail&amp;ust=1527766593219000&amp;usg=AFQjCNHsY4Z3UzSTs_bvy3TWhQ7ZdZJTtA" rel="noopener">Сукні, сарафани з вишивкою</a></h3>
                            <h3 style="text-align: center;"><a href="http://bombayshop.com.ua/sukni" style="color: #99823f;" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=uk&amp;q=http://bombayshop.com.ua/sukni&amp;source=gmail&amp;ust=1527766593219000&amp;usg=AFQjCNGLGgpEmSaHvnK5j0nJ1ivDYXgN4Q" rel="noopener">Сукні і сарафани</a></h3>
                            <h3 style="text-align: center;"><a href="http://bombayshop.com.ua/vyshyti_tyniku_i_bluzy" style="color: #99823f;" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=uk&amp;q=http://bombayshop.com.ua/vyshyti_tyniku_i_bluzy&amp;source=gmail&amp;ust=1527766593219000&amp;usg=AFQjCNG-o072EdjN46Uy8W-18U48hVKk-g" rel="noopener">Вишиті туніки і блузи</a></h3>
                            <h3 style="text-align: center;"><a href="http://bombayshop.com.ua/tyniku_i_bluzy" style="color: #99823f;" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=uk&amp;q=http://bombayshop.com.ua/tyniku_i_bluzy&amp;source=gmail&amp;ust=1527766593219000&amp;usg=AFQjCNF_dQU7K29JGrp7hfT5luB46z83wQ" rel="noopener">Туніки і блузи</a></h3>
                            <h3 style="text-align: center;"><a href="http://bombayshop.com.ua/metal" style="color: #99823f;" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=uk&amp;q=http://bombayshop.com.ua/metal&amp;source=gmail&amp;ust=1527766593219000&amp;usg=AFQjCNE_147jKs1FWaP2KP5FyuX0r4qiaA" rel="noopener">Намиста, вироби з металу </a></h3>
                            <h3 style="text-align: center;"></h3>
                            <h2 style="text-align: center; padding-bottom: 20px; font-family: Georgia; color: #793b14;"><strong><em>Заходьте та обирайте те, що Вам до вподоби!</em></strong></h2>
                            </div>""",

        }
    ]
}
print(mailjet.send.create(data=data).text)

'https://postimages.org/'
'https://s15.postimg.cc/97qm3tzez/bombay.jpg'
