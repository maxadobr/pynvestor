#include <stdio.h>

#define tributacoes 5

void mensal (float meses, float valor);

typedef struct
{
    float min[tributacoes];
    float max[tributacoes];
    float aliquota[tributacoes];
} tabela_impostos;

typedef struct
{
    float cdi;
    float selic;
    float cdb;
    float lci;
} tipos_investimentos;


void main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Uso: ./rendimentos VALOR\n");
    }

    tabela_impostos impostos = {
        .min = {0.0, 2259.21, 2826.66, 3751.06, 4664.68},
        .max = {2259.20, 2826.65, 3751.05, 4664.68, 0.00},
        .aliquota = {0.0, 0.075, 0.15, 0.225, 0.275}
    };

    tipos_investimentos investimentos = {
        .cdi = 11.46,
        .selic = 14.75,
        .cdb = 0.0,
        .lci = 0.0
    };

    float meses = atoi(argv[2]);
    float valor = atoi(argv[3]);

    mensal(meses, valor);
}

void mensal (float meses, float valor)
{
    printf("Valor: R$ %.2f\n", valor);
}