package com.creative.todoApi.service;

import com.creative.todoApi.dto.TodoDto;
import com.creative.todoApi.entity.Todo;
import com.creative.todoApi.repository.TodoRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
@Transactional(readOnly = true)
@AllArgsConstructor
public class TodoService {
    private final TodoRepository todoRepository;

    public List<TodoDto> findAll() {
        return todoRepository.findAll().stream()
                .map(TodoDto::of)
                .collect(Collectors.toList());
    }

    public TodoDto findTodo(Long id) {
        Todo todo = todoRepository.findById(id).orElseThrow();
        return TodoDto.of(todo);
    }

    @Transactional
    public void insert(String content) {
        Todo todo = Todo.create(content);
        todoRepository.save(todo);
    }

    @Transactional
    public void updateTodo(Long id, Optional<String> content, Optional<Boolean> done) {
        Todo todo = todoRepository.findById(id).orElseThrow();
        content.ifPresent(todo::setContent);
        done.ifPresent(todo::setDone);
    }

    @Transactional
    public void deleteTodo(Long id) {
        Todo todo = todoRepository.findById(id).orElseThrow();
        todoRepository.delete(todo);
    }
}