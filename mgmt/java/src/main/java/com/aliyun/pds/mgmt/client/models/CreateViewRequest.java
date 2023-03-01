// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Create view request
 */
public class CreateViewRequest extends TeaModel {
    /**
     * <p>category</p>
     */
    @NameInMap("category")
    @Validation(required = true)
    public String category;

    /**
     * <p>description</p>
     */
    @NameInMap("description")
    public String description;

    /**
     * <p>name</p>
     */
    @NameInMap("name")
    @Validation(required = true)
    public String name;

    /**
     * <p>owner</p>
     */
    @NameInMap("owner")
    @Validation(required = true)
    public String owner;

    /**
     * <p>user_id</p>
     */
    @NameInMap("user_id")
    public String userId;

    public static CreateViewRequest build(java.util.Map<String, ?> map) throws Exception {
        CreateViewRequest self = new CreateViewRequest();
        return TeaModel.build(map, self);
    }

    public CreateViewRequest setCategory(String category) {
        this.category = category;
        return this;
    }
    public String getCategory() {
        return this.category;
    }

    public CreateViewRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public CreateViewRequest setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public CreateViewRequest setOwner(String owner) {
        this.owner = owner;
        return this;
    }
    public String getOwner() {
        return this.owner;
    }

    public CreateViewRequest setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}
