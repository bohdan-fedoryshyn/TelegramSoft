package com.Rpg.repository;

import com.Rpg.entity.Project;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProjectRepo extends JpaRepository<Project, Long> {

    Project getById(Long id);
}
