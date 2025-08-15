import random

import time



def combate():

    print("⚔️ COMBATE INICIADO! ⚔️")

    time.sleep(3)

   

    # Valores iniciais

    invasao = random.randint(2, 3)

    barreiras = 4  # 4 das 17 barreiras

    plantacoes = 7 # 5% dos goblins queimarem, mas não para sempre. Graças a Deus

    dano_moradores = 0



    print(f"\nQuantidade de invasões: {invasao}")

    print(f"Barreiras do grupo: {barreiras}")

    print(f"Plantações: {plantacoes}")

    time.sleep(3)

   

    for rodada in range(invasao):

        print(f"\n--- Rodada {rodada + 1} ---")

        goblins = random.randint(2, 5)

        print(f"{goblins} goblins apareceram!")

       

        for _ in range(goblins):

            if barreiras > 0:

                quebra = random.randint(1, 100)

                print(f"Goblin {_ +1}")

                if quebra <= 70:

                    print("⛔ Barreira resistiu! Goblin se ferrou.")

                    time.sleep(2)

                else:

                    barreiras -= 1  # Reduz o número de barreiras intactas

                    print(f"\n💥 Goblin quebrou uma barreira! \nBarreiras restantes: {barreiras}")

                    time.sleep(2)



                    enfrenta = input("Enfrentar o goblin? (sim/não): ").strip().lower() # O .strip vai tirar os espaços e outras coisas, obg pessoa que n lembro de falar sobre isso.

                    time.sleep(2)

                   

                    if enfrenta == "sim":

                        print("⚔️ Diâmica foi iniciada!")

                        # Lógica do combate direto aqui

                    else:

                        print(f"😱 Você fugiu! Moradores sofrem dano equivalente a 1")

                        dano_moradores += 1

                       

                        if random.randint(1, 100) <= 5:

                            plantacoes -= 1

                            print(f"🔥 Uma plantação foi queimada! Restantes: {plantacoes}")

            else:

                print("\n🚧 Todas as barreiras foram destruídas! \nGoblins avançam livremente!")

                enfrenta = input("Enfrentar os goblins? (sim/não): ").strip().lower()

                if enfrenta == "sim":

                    print("⚔️ Combate direto iniciado contra todos!")

                else:

                    dano_moradores += 1  # Dano por goblin que passa

                    print(f"😱 Você fugiu! Moradores sofrem dano equivalente a 1")



    vida_do_lenhador = 4

    vida_do_ferreiro = 10

    vida_do_mineiro = 10





    # Tudo que a gente precisa saber junto de time sleep

    print("\n=== FIM DO COMBATE ===")

    time.sleep(3)

    print("Resumo final:")

    time.sleep(1)

    print(f"- Barreiras intactas: {barreiras}")

    time.sleep(1)

    print(f"- Dano total aos moradores: {dano_moradores}")

    time.sleep(1)

    print(f"- Plantações restantes: {plantacoes}")

    time.sleep(1)

    print(f"- Vida dos moradores da vila do espantalho\nLenhador: {vida_do_lenhador - dano_moradores}\nFerreiro: {vida_do_ferreiro - dano_moradores}\nMineiro: {vida_do_mineiro - dano_moradores}")



combate()
