from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVsitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
                # Edith ouviu falar que agora a aplicação online de lista de tarefas

                # aceita definir prioridades nas tarefas do tipo baixa, média e alta

                # Ela decide verificar a homepage
		self.browser.get("http://localhost:8000")
                # Ela percebe que o título da página e o cabeçalho mencionam

                # listas de tarefas com prioridade (priority to-do)

		self.assertIn('priority to-do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('priority to-do', header_text)
		
                # Ela é convidada a inserir um item de tarefa e a prioridade da 

                # mesma imediatamente
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

                # Ela digita "Comprar anzol" em uma nova caixa de texto

                # e assinala prioridade alta no campo de seleção de prioridades
		inputbox.send_keys('Comprar anzol')


                # Quando ela tecla enter, a página é atualizada, e agora

                # a página lista "1 - Comprar anzol - prioridade alta"

                # como um item em uma lista de tarefas
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Comprar anzol',[row.text for row in rows])
	    
                # Ainda continua havendo uma caixa de texto convidando-a a 

                # acrescentar outro item. Ela insere "Comprar cola instantâne"

                # e assinala prioridade baixa pois ela ainda tem cola suficiente

                # por algum tempo
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Comprar cola instantânea')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

                # A página é atualizada novamente e agora mostra os dois

                # itens em sua lista e as respectivas prioridades
 
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Comprar anzol',[row.text for row in rows])
		self.assertIn('2: Comprar cola instantâneal',[row.text for row in rows])

                # Edith se pergunta se o site lembrará de sua lista. Então

                # ela nota que o site gerou um URL único para ela -- há um 

                # pequeno texto explicativo para isso.

                # Ela acessa essa URL -- sua lista de tarefas continua lá.
                self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()
