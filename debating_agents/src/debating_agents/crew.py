from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class DebatingAgents():
    """DebatingAgents crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config['debater'], # type: ignore[index]
            verbose=True
        )

    @agent
    def opponent(self) -> Agent:
        return Agent(
            config=self.agents_config['opponent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'], 
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'], 
        )

    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DebatingAgents crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
