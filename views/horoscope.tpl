<html>
    <head>
    	<meta charset='utf-8'>
    	<title>Гороскоп на сегодня</title>
        <link   rel="stylesheet"
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
                integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
                crossorigin="anonymous">
        <style type="text/css">
            .col:hover {
                background-color: lightgreen;
            }
        </style>

        <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
     </head>
    <body>
        <div class="container">
            <div class="row" style="padding-left: 10px">
                <h1 id="my_func">Ваши предсказания на {{ date }}</h1>
            </div>
            <div class="row">
                <div class="col" id="r0">
                        <p></p>
                </div>
                <div class="col" id="r1">
                        <p></p>
                </div>
                <div class="col" id="r2">
                        <p></p>
                </div>
            </div>
            <div class="row" style="padding-top: 20px">
                <div class="col" id="r3">
                        <p></p>
                </div>
                <div class="col" id="r4">
                        <p></p>
                </div>
                <div class="col" id="r5">
                        <p></p>
                </div>
            </div>
        </div>
    </body>
    <script language="javascript">
        advice_url='http://sf-pyw.mosyag.in/m04/api/forecasts'
        // advice_url='http://localhost:8080/api/forecast'
        $('#my_func').click(function(){

            $.getJSON(advice_url, function(data){
                set_secret_message(data);
            })

        })

        function set_secret_message(msg){

            r=0;
            for (ms in msg['prophecies']){
                // console.log(msg['prophecies'][ms])
                p=$('#r' + r);
                p.html(msg['prophecies'][String(r)]);
                r += 1;
            }
        }
    </script>

 </html>
