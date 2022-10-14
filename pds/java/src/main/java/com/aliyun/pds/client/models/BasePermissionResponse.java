// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 权限记录 response
 */
public class BasePermissionResponse extends TeaModel {
    @NameInMap("action_list")
    public java.util.List<BaseActionItemResponse> actionList;

    @NameInMap("collection")
    public String collection;

    @NameInMap("condition")
    public Condition condition;

    @NameInMap("created_at")
    public Long createdAt;

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

    @NameInMap("updated_at")
    public Long updatedAt;

    @NameInMap("user_tags")
    public java.util.List<String> userTags;

    public static BasePermissionResponse build(java.util.Map<String, ?> map) throws Exception {
        BasePermissionResponse self = new BasePermissionResponse();
        return TeaModel.build(map, self);
    }

    public BasePermissionResponse setActionList(java.util.List<BaseActionItemResponse> actionList) {
        this.actionList = actionList;
        return this;
    }
    public java.util.List<BaseActionItemResponse> getActionList() {
        return this.actionList;
    }

    public BasePermissionResponse setCollection(String collection) {
        this.collection = collection;
        return this;
    }
    public String getCollection() {
        return this.collection;
    }

    public BasePermissionResponse setCondition(Condition condition) {
        this.condition = condition;
        return this;
    }
    public Condition getCondition() {
        return this.condition;
    }

    public BasePermissionResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public BasePermissionResponse setEffect(String effect) {
        this.effect = effect;
        return this;
    }
    public String getEffect() {
        return this.effect;
    }

    public BasePermissionResponse setIdentityId(String identityId) {
        this.identityId = identityId;
        return this;
    }
    public String getIdentityId() {
        return this.identityId;
    }

    public BasePermissionResponse setIdentityType(String identityType) {
        this.identityType = identityType;
        return this;
    }
    public String getIdentityType() {
        return this.identityType;
    }

    public BasePermissionResponse setResource(String resource) {
        this.resource = resource;
        return this;
    }
    public String getResource() {
        return this.resource;
    }

    public BasePermissionResponse setResourceType(String resourceType) {
        this.resourceType = resourceType;
        return this;
    }
    public String getResourceType() {
        return this.resourceType;
    }

    public BasePermissionResponse setUpdatedAt(Long updatedAt) {
        this.updatedAt = updatedAt;
        return this;
    }
    public Long getUpdatedAt() {
        return this.updatedAt;
    }

    public BasePermissionResponse setUserTags(java.util.List<String> userTags) {
        this.userTags = userTags;
        return this;
    }
    public java.util.List<String> getUserTags() {
        return this.userTags;
    }

}
