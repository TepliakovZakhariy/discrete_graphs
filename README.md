# discrete_graphs

# Звіт

### Розподіл роботи

- **read_graph** - Тепляков Захарій
- **hamiltonian_cycle** - Тепляков Захарій
- **eulerian_cycle** - Сидорчук Софія
- **check_isomorphism** - Вітковська Анна-Марія
- **check_bipartite** - Халус Анастасія
- **color_graph** - Гнатів Анна

### Функції

#### read_graph

#### hamiltonian_cycle

#### eulerian_cycle

#### check_isomorphism

Функція "check_isomorphism" перевіряє, чи є два графіки, представлені у вигляді словників, ізоморфними.  
Підфункції:

1. Функція "graph_matrix_creation": ця допоміжна функція перетворює словник графа на матрицю суміжності. Вона створює квадратну матрицю numpy, де кожна клітинка [i, j] має значення "1", якщо між вершинами "i" та "j" є ребро, і "0" в протилежному випадку.
2. Функція "matrix_change": голона для алгоритму перебору перестановок; функція застосовує перестановку до рядків і стовпців матриці суміжності графіка. Приймає граф, початкову перестановку та поточну. Присвоює значення поточної перестановки матриці графа - і по рядках, і по стовпцях за допомогою розпакування.
3. Функції для перевірки інваріантів: - "check_vertices_number_inv": перевіряє, чи обидва графи мають однакову кількість вершин, порівнюючи довжини словників. - "check_edges_number_inv": перевіряє, чи обидва графи мають однакову кількість ребер, рахуючи загальну довжину списків у значеннях словника. - "chech_degrees_of_vertices": перевіряє, чи обидва графи мають однакові степені вершин, рахуючи значення кожної через довжину значень словника.
   Інваріанти мають вирішальне значення для швидкого виключення неізоморфних графів без необхідності перевіряти всі перестановки.
   Логіка перестановок і порівнянь: після перевірки інваріантів функція генерує всі можливі перестановки набору вершин (за допомогою itertools.permutations). Перетворивши обидва графи в матриці, вона створює початкову перестановку в правильному порядку, після чого через генератор permutations починає її переставляти. Максимальна кількість перестановок - факторіал кількості вершин. Перебираємо усі варіанти викликавши наступну перестановку через next, та передавши її у "matrix_change". Якщо на якомусь із кроків перша матриця дорівнює матриці другого графа, тоді їхній ізоморфізм доведно, тож повертаємо True. Якщо такої перестановки не знайдено - False.
   Використання "numpy" і "deepcopy": "numpy" використовується для ефективних маніпуляцій з масивами, адже вони набагато швидші за звичні списки; "deepcopy" гарантує, що вихідна матриця суміжності першого графіка не буде змінена під час тестування перестановки.

#### check_bipartite

#### color_graph
