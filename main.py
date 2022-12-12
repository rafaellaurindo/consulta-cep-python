import requests

def main():
	print('####################')
	print('### Consulta CEP ###')
	print('####################')
	print()

	
	while True:
		try:

			cep_input = input('Digite o CEP para a consulta (Deve conter apenas números): ')

			if len(cep_input) != 8:
				raise ValueError("O CEP deve conter 8 dígitos")

		except ValueError as e:
			print("valor inválido para cep. ", e)
		
		else:
			break
		
		
	
	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

	address_data = request.json()

	if 'erro' not in address_data:
		print('==> CEP ENCONTRADO <==')
		
		print('CEP: {}'.format(address_data['cep']))
		print('Logradouro: {}'.format(address_data['logradouro']))
		print('Complemento: {}'.format(address_data['complemento']))
		print('Bairro: {}'.format(address_data['bairro']))
		print('Cidade: {}'.format(address_data['localidade']))
		print('Estado: {}'.format(address_data['uf']))
		print("\n")
		
	else:
		print('{}: CEP inválido.'.format(cep_input))

	print('---------------------------------')

	while True:
		try:

			option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
			if option == 1:
				main()
			else:
				print('Saindo...')

			if len(cep_input) != 8:
				raise ValueError("Informe um valor válido")

		except ValueError as e:
			print("Opção inválida. Digite 1 ou 2.")
		
		else:
			break
	

if __name__ == '__main__':
	main()