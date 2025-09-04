from flask import Flask, render_template, request
import random

app = Flask(__name__)

def decimal_a_gms(decimal):
    grados = int(decimal)
    minutos_float = abs(decimal - grados) * 60
    minutos = int(minutos_float)
    segundos = round((minutos_float - minutos) * 60, 2)
    return grados, minutos, segundos

coordenadas = [
    decimal_a_gms(-34.61) + decimal_a_gms(-58.38),   # Argentina
    decimal_a_gms(-15.78) + decimal_a_gms(-47.93),   # Brasil
    decimal_a_gms(40.42) + decimal_a_gms(-3.70),     # España
    decimal_a_gms(19.43) + decimal_a_gms(-99.13),    # México
    decimal_a_gms(35.68) + decimal_a_gms(139.69)     # Japón
]

@app.route("/", methods=["GET", "POST"])
def juego():
    lat_g, lat_m, lat_s, lon_g, lon_m, lon_s = random.choice(coordenadas)
    return render_template(
        "index.html",
        lat_g=lat_g, lat_m=lat_m, lat_s=lat_s,
        lon_g=lon_g, lon_m=lon_m, lon_s=lon_s
    )

if __name__ == "__main__":
    app.run(debug=True)
