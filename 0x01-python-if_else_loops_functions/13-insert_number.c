#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node in a sorted linked list.
 * @head: Pointer to the linked list.
 * @number: The number to add to the list.
 *
 * Return: The address of the new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (*head && (*head)->n < number)
		head = &(*head)->next;
	new->next = *head;
	*head = new;

	return (new);
}
