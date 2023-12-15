# discrete_graphs

# Звіт

### Розподіл роботи

- **read_graph** - Тепляков Захарій
- **hamiltonian_cycle** - Тепляков Захарій
- **eulerian_cycle** - Сидорчук Софія
- **check_isomorphism** - Вітковська Анна-Марія
- **check_bipartite** - Халус Анастасія
- **color_graph** - Гнатів Анна
- **Звіт** - усі учасники
- **Презентація** - усі учасники

### Функції

#### read_graph

Функція read_graph_from_file приймає аргумент filepath, який є рядком і представляє шлях до файлу. Функція повертає граф у вигляді словника.

Потім функція ініціалізує порожній словник graph, який буде використовуватися для збереження графа.

Функція відкриває файл, вказаний у filepath, та для кожного рядка у файлі, функція видаляє можливі пробіли в рядку (strip()) і розділяє його на дві вершини графа за комою.

Функція намагається змінити тип значень вершин на int. Якщо зміна неможлива, виникає виняток ValueError.

Функція додає вершину vertex2 до списку суміжних вершин для вершини vertex1 у словнику graph.

Функція повертає словник з відсортованими ключами та значеннями.

#### hamiltonian_cycle

Функція hamiltonian_cycle приймає аргумент graph та повертає або список вершин (якщо знайдено гамільтонів цикл), або None (якщо гамільтонів цикл не існує).

Функція розпочинається перевіркою, щоб забезпечити, що граф не є порожнім (not graph) і що всі вершини в графі мають принаймні одну суміжну вершину (not all(graph.values())). Якщо ці умови не виконуються, функція повертає None.

Функція ініціалізує змінну start_node - перша вершина у графі і створює порожній список path для збереження шляху в підфункції dfs_hamiltonian_cycle.

Функція dfs_hamiltonian_cycle приймає два параметри: node, який представляє поточну вершину у графі, і path, який представляє поточний шлях. Вона повертає або список (якщо знайдено гамільтонів цикл), або None (якщо гамільтонів цикл не існує).

Кроки виконання dfs_hamiltonian_cycle:

1.  Функція додає поточну вершину до path.
2.  Якщо довжина path дорівнює кількості вершин у графі, вона перевіряє, чи існує ребро від останньої вершини в шляху до початкового вузла (start_node). Якщо таке ребро існує, знайдено гамільтонів цикл, і функція повертає повний шлях. Інакше вона повертає None.
3.  Якщо шлях не є повним, функція ітерується через суміжні вершини поточної вершини. Якщо суміжна вершина ще не була відвідана, функція рекурсивно викликається з цією вершиною і та копією шляху. Якщо гамільтонів цикл знайдено у рекурсії, функція повертає результат.
4.  Якщо всі суміжні вже відвідані або рекурсивні виклики повернули None, функція повертає None.

На завершення функція hamiltonian_cycle запускає DFS, викликаючи dfs_hamiltonian_cycle з початковим вузлом і порожнім шляхом.

#### eulerian_cycle

Функція is_connected перевіряє граф на зв’язність. Функція містить підфункцію яка працює рекурсивно використовуючи алгоритм пошуку в глибину. is_connected повертає True або False в залежності від того, чи існує вершина яка не була відвідана.
Ще одна функція яка перевіряє чи можливо будувати Ейлерів цикл це функція – перевірка на парність степенів.  
В основній функції ми перевіряємо за допомогою двох функцій вище чи всі степені парні а вершини відвідані та якщо це так, будуємо цикл. Алгоритм побудови використовує стек, і відстежує пройдені ребра за допомогою функції для запису тих, які ми вже проходили.

#### check_isomorphism

Функція "check_isomorphism" перевіряє, чи є два графіки, представлені у вигляді словників, ізоморфними.

Підфункції:

1. Функція "graph_matrix_creation": ця допоміжна функція перетворює словник графа на матрицю суміжності. Вона створює квадратну матрицю numpy, де кожна клітинка [i, j] має значення "1", якщо між вершинами "i" та "j" є ребро, і "0" в протилежному випадку.

2. Функція "matrix_change": голона для алгоритму перебору перестановок; функція застосовує перестановку до рядків і стовпців матриці суміжності графіка. Приймає граф, початкову перестановку та поточну. Присвоює значення поточної перестановки матриці графа - і по рядках, і по стовпцях за допомогою розпакування.

3. Функції для перевірки інваріантів:

- "check_vertices_number_inv": перевіряє, чи обидва графи мають однакову кількість вершин, порівнюючи довжини словників.
- "check_edges_number_inv": перевіряє, чи обидва графи мають однакову кількість ребер, рахуючи загальну довжину списків у значеннях словника.
- "chech_degrees_of_vertices": перевіряє, чи обидва графи мають однакові степені вершин, рахуючи значення кожної через довжину значень словника.

Інваріанти мають вирішальне значення для швидкого виключення неізоморфних графів без необхідності перевіряти всі перестановки.

Логіка перестановок і порівнянь: після перевірки інваріантів функція генерує всі можливі перестановки набору вершин (за допомогою itertools.permutations). Перетворивши обидва графи в матриці, вона створює початкову перестановку в правильному порядку, після чого через генератор permutations починає її переставляти. Максимальна кількість перестановок - факторіал кількості вершин. Перебираємо усі варіанти викликавши наступну перестановку через next, та передавши її у "matrix_change". Якщо на якомусь із кроків перша матриця дорівнює матриці другого графа, тоді їхній ізоморфізм доведно, тож повертаємо True. Якщо такої перестановки не знайдено - False.

Використання "numpy" і "deepcopy": "numpy" використовується для ефективних маніпуляцій з масивами, адже вони набагато швидші за звичні списки; "deepcopy" гарантує, що вихідна матриця суміжності першого графіка не буде змінена під час тестування перестановки.

#### check_bipartite

Функція check_bipartite використовує метод глибинного першого пошуку
(DFS) для визначення двудольності графа.

- Функція перевіряє наявність графа. Якщо граф відсутній (пустий), повертається False.
  - У функції застосовується алгоритм DFS для проходження графа, починаючи з кожної вершини.
  - Відвідувані вершини позначаються та розфарбовуються в два кольори (0 та 1), щоб визначити дві частини (двудольність) графа.
  - Під час проходження перевіряється, чи вершини, які з'єднані ребром, мають різні кольори (розфарбування), що підтверджує двочастковість графа.
  - Якщо знайдено вершину, що порушує умови двочастковості (з'єднана з вершиною того ж кольору), функція повертає False.
  - Після проходження всіх вершин графа, якщо не виявлено порушень двудольності, функція повертає True.

#### color_graph

Функція color_graph реалізує алгоритм розфарбовування графа за принципом, що жодні два сусідні вершини не можуть мати однаковий колір. Аргументом функції є граф у вигляді словника, де ключі - це вершини, а значення - списки сусідніх вершин.

Кроки виконання:

1. Ініціалізація змінних:

   - colors: словник, що зберігає відображення вершини у її колір.
   - colored_vertices: список кортежів (вершина, колір), що зберігає відображення вершин та їхніх кольорів.

2. Ітерація по кожній вершині графа:
   - Для кожної вершини визначається множина вже використаних кольорів (used_colors).
3. Перевірка кольорів сусідніх вершин:
   - Перевіряється колір кожної сусідньої вершини. Якщо вершина вже розфарбована, її колір додається до множини used_colors.
4. Розфарбовування поточної вершини:
   - Шукається перший доступний колір для поточної вершини (не використаний в used_colors). Якщо знайдено, вершина розфарбовується цим кольором і пара (вершина, колір) додається до colored_vertices. Якщо доступних кольорів немає, функція повертає рядок False.
