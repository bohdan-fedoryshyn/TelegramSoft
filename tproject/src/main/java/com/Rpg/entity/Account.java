package com.Rpg.entity;

import javax.persistence.*;

public class Account {

    @Id
    private Long id;

    @Column
    private String name;

    @Enumerated(EnumType.STRING)
    private Status status;

    @ManyToOne
    private Project project;
}
