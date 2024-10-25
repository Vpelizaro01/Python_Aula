
import math

def pi():
    return 3.14


def main():
   
    raio = float(input("Qual é o raio da circunferência? "))

   
    area = math.pow(raio, 2.0) * pi()


    print(f"\nA área da circunferência é: {area}")

if __name__ == "__main__":
    main()
