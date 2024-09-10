// Exercicio-01
class Program
{
    static void Main(string[] args)
    {
        Console.Write("Digite um número entre 1 e 10: ");
        int numero = Convert.ToInt32(Console.ReadLine());
        string numeroPorExtenso = ObterNumeroPorExtenso(numero);
        Console.WriteLine($"Número por extenso é: {numeroPorExtenso}");
        Console.ReadKey();
    }

    static string ObterNumeroPorExtenso(int numero)
    {
        switch (numero)
        {
            case 1: return "Um";
            case 2: return "Dois";
            case 3: return "Três";
            case 4: return "Quatro";
            case 5: return "Cinco";
            case 6: return "Seis";
            case 7: return "Sete";
            case 8: return "Oito";
            case 9: return "Nove";
            case 10: return "Dez";
            default: return "Número inválido.";
        }
    }
}

// Exercicio-02
class OperacoesMatematicas
{
    static double Divide(int x, int y)
    {
        return (double)x / y;
    }

    static double Multiplica(int x, int y)
    {
        return x * y;
    }

    static double Adicao(int x, int y)
    {
        return x + y;
    }

    static double Subtrai(int x, int y)
    {
        return x - y;
    }

    static int Main(string[] args)
    {
        Console.WriteLine("Insira um número para realizar a operação:");
        int x = int.Parse(Console.ReadLine());
        Console.WriteLine("Insira outro número para realizar a operação:");
        int y = int.Parse(Console.ReadLine());
        Console.Write("Insira: 1=divisão\t2=multiplicação\t3=adição\t4=subtração: ");
        int z = int.Parse(Console.ReadLine());

        double resultado;
        switch (z)
        {
            case 1:
                resultado = Divide(x, y);
                Console.WriteLine("O resultado da sua divisão é: " + resultado);
                break;
            case 2:
                resultado = Multiplica(x, y);
                Console.WriteLine("O resultado da sua multiplicação é: " + resultado);
                break;
            case 3:
                resultado = Adicao(x, y);
                Console.WriteLine("O resultado da sua adição é: " + resultado);
                break;
            case 4:
                resultado = Subtrai(x, y);
                Console.WriteLine("O resultado da sua subtração é: " + resultado);
                break;
            default:
                Console.WriteLine("Opção inválida.");
                break;
        }

        return 0;
    }
}

// Exercicio-03
class ValidacaoCPF
{
    static void Main(string[] args)
    {
        Console.WriteLine("Insira o seu CPF: ");
        string cpf = Console.ReadLine();
        if (ValidarFormatoDoCpf(cpf))
        {
            if (ValidacaoCPF(cpf))
            {
                Console.WriteLine("CPF válido");
            }
            else
            {
                Console.WriteLine("CPF inválido");
            }
        }
        else
        {
            Console.WriteLine("Formato inválido de CPF");
        }
    }

    static bool ValidarFormatoDoCpf(string cpf)
    {
        if (cpf.Length != 14) return false;
        for (int i = 0; i < cpf.Length; i++)
        {
            if ((i == 3 || i == 7) && cpf[i] != '.') return false;
            else if (i == 11 && cpf[i] != '-') return false;
            else if (i != 3 && i != 7 && i != 11 && !char.IsDigit(cpf[i])) return false;
        }
        return true;
    }

    static bool ValidacaoCPF(string cpf)
    {
        int[] usuario01 = { 10, 9, 8, 7, 6, 5, 4, 3, 2 };
        int[] usuario02 = { 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 };
        string cpfqntnumeros = cpf.Replace(".", "").Replace("-", "");
        if (cpfqntnumeros.Length != 11) return false;

        int somaNumeros01 = 0;
        for (int i = 0; i < 9; i++)
        {
            somaNumeros01 += (cpfqntnumeros[i] - '0') * usuario01[i];
        }
        int divisao01 = (somaNumeros01 * 10) % 11;

        return true; 
    }
}
