package com.Rpg.entity;

import javax.xml.crypto.Data;

public class Task {

    Task(Type type) {
        this.type = type;
    }

    private Type type;

    private Data creation;

    private Status status;

}
