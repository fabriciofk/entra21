import datamanager
import person
import bank


def main():
    # 4 - Fazer depósito
    # account_number = input('Digite o número da conta: ')
#     # deposit_value = float(input('Digite o valor do depósito: '))
#     #
#     # # Recuperando os dados do arquivo
#     # data_reader = datamanager.DataReader('bankaccounts.csv')
#     # object_list = data_reader.get_data()
#     #
#     # for obj in object_list:
#     #     if obj.account_number == account_number:
#     #         obj.make_deposit(deposit_value)
#     #         break
#     #
#     # data_writer = datamanager.DataWriter('bankaccounts.csv')
#     # data_writer.update_data(object_list)
    pessoa = person.Person('William', 20, '110-814-329-69')
    pessoa.save_person()
    banco = bank.Bank(1, 'Bradesco')
    conta = bank.BankAccount(pessoa, 1234, banco, 112313, 1232, 1000.00)
    conta.save_bankaccount()

if __name__ == '__main__':
    # pessoa = person.Person('William', 20, '111-111-111-11')
    # banco = bank.Bank(1, 'Viacredi')
    # conta = bank.BankAccount(pessoa, 123456, banco, 123456, 1111, 10)
    #
    # datawriter = datamanager.DataWriter('bankaccounts.csv')
    # datawriter.save_data(conta)

    main()


