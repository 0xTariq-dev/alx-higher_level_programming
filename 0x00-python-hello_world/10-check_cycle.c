#include "lists.h"

/**
 * check_cycle - Checks if a linked list is circular or not.
 * @list: A pointer to the list struct.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *new;

	current = list;
	new = list->next;

	while (current && new && new->next)
	{
		if (current == new)
			return (1);
		current = current->next;
		new = new->next->next;
	}
	return (0);
}
