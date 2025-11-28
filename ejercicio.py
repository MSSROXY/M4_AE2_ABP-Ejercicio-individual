class TarjetaCredito:
    tarjetas = []
    # Incluye en este método valores por default

    def __init__(self, limite_credito, intereses, saldo_pagar=0):

        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta rechazada: has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas_tarjetas(cls):
        for tarjeta in cls.tarjetas:
            print(
                f"Tarjeta -> Límite: {tarjeta.limite_credito}, Saldo: {tarjeta.saldo_pagar}, Interes: {tarjeta.intereses}")


t1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
t2 = TarjetaCredito(limite_credito=5000, intereses=0.03)
t3 = TarjetaCredito(3000, 0.05)


t1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()
t2.compra(500).compra(300).compra(1000).pago(200).pago(150).cobrar_interes().mostrar_info_tarjeta()
t3.compra(1200).compra(800).compra(200).compra(400).compra(500).mostrar_info_tarjeta()

TarjetaCredito.mostrar_todas_tarjetas()
