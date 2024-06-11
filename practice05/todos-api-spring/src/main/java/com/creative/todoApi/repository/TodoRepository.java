package com.creative.todoApi.repository;

import com.creative.todoApi.entity.Todo;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TodoRepository extends JpaRepository<Todo, Long> {
    @Override
    List<Todo> findAll();
}
