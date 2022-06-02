package com.Rpg.entity;

import lombok.Data;

import javax.persistence.*;
import java.util.List;

@Entity
@Data
@Table(name = "project")
public class Project {

    @Id
    Long id;

    @Column
    String description;

    @Column
    String name;

    @OneToMany(mappedBy = "project", cascade = CascadeType.ALL)
    private List<Account> accounts;

    @ManyToOne
    private User user;

}
