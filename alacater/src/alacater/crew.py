from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai.knowledge.source.crew_docling_source import CrewDoclingSource




@CrewBase
class Alacater():
	"""Alacater crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'




	
	@agent
	def ninive_menu_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['ninive_menu_finder'],
			verbose=True,


		)

	@task
	def ninive_menu_finding_task(self) -> Task:
		return Task(
			config=self.tasks_config['ninive_menu_finding_task'],
			output_file='report.md',
		)
	
	

	@crew
	def crew(self) -> Crew:
		"""Creates the Alacater crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,

			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
