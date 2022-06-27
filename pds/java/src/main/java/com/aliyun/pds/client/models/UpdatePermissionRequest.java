// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * request
 */
public class UpdatePermissionRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("action_list")
    public java.util.List<BaseActionItemRequest> actionList;

    @NameInMap("collection")
    public String collection;

    @NameInMap("condition")
    public Condition condition;

    @NameInMap("effect")
    public String effect;

    @NameInMap("identity_id")
    public String identityId;

    @NameInMap("identity_type")
    public String identityType;

    @NameInMap("resource")
    public String resource;

    @NameInMap("resource_type")
    public String resourceType;

    @NameInMap("user_tags")
    public java.util.List<String> userTags;

    public static UpdatePermissionRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdatePermissionRequest self = new UpdatePermissionRequest();
        return TeaModel.build(map, self);
    }

    public UpdatePermissionRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdatePermissionRequest setActionList(java.util.List<BaseActionItemRequest> actionList) {
        this.actionList = actionList;
        return this;
    }
    public java.util.List<BaseActionItemRequest> getActionList() {
        return this.actionList;
    }

    public UpdatePermissionRequest setCollection(String collection) {
        this.collection = collection;
        return this;
    }
    public String getCollection() {
        return this.collection;
    }

    public UpdatePermissionRequest setCondition(Condition condition) {
        this.condition = condition;
        return this;
    }
    public Condition getCondition() {
        return this.condition;
    }

    public UpdatePermissionRequest setEffect(String effect) {
        this.effect = effect;
        return this;
    }
    public String getEffect() {
        return this.effect;
    }

    public UpdatePermissionRequest setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public UpdatePermissionRequest setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public UpdatePermissionRequest setResource(String resource) {
        this.resource = resource;
        return this;
    }
    public String getResource() {
        return this.resource;
    }

    public UpdatePermissionRequest setResourceType(String resourceType) {
        this.resourceType = resourceType;
        return this;
    }
    public String getResourceType() {
        return this.resourceType;
    }

    public UpdatePermissionRequest setUserTags(java.util.List<String> userTags) {
        this.userTags = userTags;
        return this;
    }
    public java.util.List<String> getUserTags() {
        return this.userTags;
    }

}
