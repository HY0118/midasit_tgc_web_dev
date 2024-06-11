package com.creative.todoApi.entity;

import lombok.Getter;

import javax.persistence.*;

@Entity
@Getter
public class Todo {
    @Id
    @GeneratedValue(
            strategy = GenerationType.IDENTITY
    )
    private Long id;
    @Column(
            length = 512,
            nullable = false
    )
    private String content;
    @Column
    private Boolean done;

    ////////////////////////////////////////////////////////

    public static Todo create(String content) {
        Todo inst = new Todo();
        inst.content = content;
        inst.done = false;
        return inst;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void setDone(Boolean done) {
        this.done = done;
    }
}
