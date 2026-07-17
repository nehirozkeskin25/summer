class MeyveSepeti:
    def __init__(self, meyveler):
        self.meyveler = meyveler
        self.indeks = 0

    def __iter__(self):
        self.indeks = 0  
        return self

    def __next__(self):
        if self.indeks >= len(self.meyveler):
            raise StopIteration  
        meyve = self.meyveler[self.indeks]
        self.indeks += 1
        return meyve


if __name__ == "__main__":
    sepet = MeyveSepeti(["elma", "muz", "çilek", "karpuz", "kiraz"])

    print("sepetteki meyveler:")
    for meyve in sepet:
        print(f"{meyve}")

   
    print("\nİkinci tur:")
    for meyve in sepet:
        print(f"{meyve}")