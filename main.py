#создем поле
field = list(range(1, 10))
# "рисуем" поле для игры, создав функцию
def draw_field(battle_field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-" * 13)
# Взаимодействие с пользователем. Сбор и проверка информации от игрока.
def take_input(player_input): #функция принимающая ввод пользователя
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_input+"?(Введите число от 1 до 9): ")
      try: # блок try/except обрабатывающий исключения
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Введите число от 1 до 9.") # если вместо цифры введен другой символ
         continue
      if player_answer >= 1 and player_answer <= 9: #проверяем входил ли число в диапазон от 1 до 9
         if(str(field[player_answer-1]) not in "XO"): #проверяем свободна ли клетка
            field[player_answer-1] = player_input
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")
# Функция проверки игрового поля. Проверяет выиграл ли игрок.
def check_win(field):
   win_comb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # выигрышные комбинации
   for each in win_comb:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False
# заводим функцию-счетчик
def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
           take_input("X") # первый пользователь
        else:
           take_input("O") # второй пользователь
        counter += 1
        if counter > 4: # создаем условие чтобы лишний раз не вызывать функцию check_win
           tmp = check_win(field)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_field(field)
main(field)
input("Нажмите Enter для выхода!")
