<h1>Mealy's and Moore's machines and work with them</h1>
<h2>Task 1: ✅</h2>     
<ol>
    <li>Реалізувати клас MealyMachine для симуляції роботи довільного автомата Мілі, який повинен:
        <ol>
            <li>Опрацьовувати вхідний рядок та видавати вихідний рядок.</li>
            <li>Відображати таблицю переходів під час обробки.</li>
            <li>Підтримувати гнучку зміну конфігурації (вхідний алфавіт, стани, функція переходів).</li>
        </ol>
    </li>
    <li>Налаштувати та протестувати автомат Мілі для наступного сценарію:
        <ul>
            <li>Вхідний алфавіт: {a, b}</li>
            <li>Стани: {S0, S1}</li>
            <li>Функція переходів:
                <ul>
                    <li>S0 → S1 при a (вихід 0)</li>
                    <li>S0 → S0 при b (вихід 0)</li>
                    <li>S1 → S1 при a (вихід 0)</li>
                    <li>S1 → S0 при b (вихід 1)</li>
                </ul>
            </li>
            <li>Початковий стан: S0</li>
        </ul>
    </li>
    <li>Реалізувати можливість збереження стану у форматі JSON та повторного запуску автомата.     
        <pre>
Mealy.json:
{
    "current_state": "S0",
    "history": [
        ["S0", "a", "0"],
        ["S1", "a", "0"],
        ["S1", "b", "1"],
        ["S0", "b", "0"]
    ]
}
        </pre>
    </li>
</ol>
<h2>Task 2: ✅</h2>           
  Написати програму, що приймає на вхід автомат Мура та переводить його в еквівалентний
  автомат Мілі. Протестувати на власних прикладах.
<h4>Subject: Methods of projecting algorythms</h4>
<h4>University: National University of "Kyiv-Mohyla Academy"</h4>

<h1>Find all sums <i>S</i> in list <i>arr</i></h1>
<h2>Main task: ✅</h2>
<ul>
    <li>
        Function takes list of numbers and sum as input and returns all sums, that are present in list       
    </li>
    <li>
        Function must be written in a recursive way          
    </li>
</ul>
<h2>Side tasks</h2>
<ul>
    <li>
        Write docstring for the function
    </li>
    <li>
        Write unit tests for the function
    </li>
    <li>
        Calculate time-complexity of the algorythm using big O-notation
    </li>
</ul>

