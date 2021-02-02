// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class AddStoreResponse extends TeaModel {
    // 全球加速地址
    @NameInMap("accelerate_endpoint")
    public String accelerateEndpoint;

    // 存储公共前缀
    @NameInMap("base_path")
    public String basePath;

    // bucket名称
    @NameInMap("bucket")
    @Validation(required = true)
    public String bucket;

    // 内容分发地址
    @NameInMap("cdn_endpoint")
    public String cdnEndpoint;

    // 自定义全球加速地址
    @NameInMap("customized_accelerate_endpoint")
    public String customizedAccelerateEndpoint;

    // 自定义内容分发地址
    @NameInMap("customized_cdn_endpoint")
    public String customizedCdnEndpoint;

    // 自定义Public访问地址
    @NameInMap("customized_endpoint")
    public String customizedEndpoint;

    // 自定义vpc访问地址
    @NameInMap("customized_internal_endpoint")
    public String customizedInternalEndpoint;

    // domain ID
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    // Public访问地址
    @NameInMap("endpoint")
    @Validation(required = true)
    public String endpoint;

    // vpc访问地址
    @NameInMap("internal_endpoint")
    public String internalEndpoint;

    // 地点
    @NameInMap("location")
    public String location;

    // 存储归属，system表示系统提供，custom表示使用自己的存储
    @NameInMap("ownership")
    @Validation(required = true)
    public String ownership;

    // Policy授权,system类型store会将bucket权限授予当前云账号
    @NameInMap("policy")
    @Validation(required = true)
    public String policy;

    // 访问Bucket的角色ARN
    @NameInMap("role_arn")
    public String roleArn;

    // store ID
    @NameInMap("store_id")
    @Validation(required = true)
    public String storeId;

    // 存储类型，当前只支持oss
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static AddStoreResponse build(java.util.Map<String, ?> map) throws Exception {
        AddStoreResponse self = new AddStoreResponse();
        return TeaModel.build(map, self);
    }

    public AddStoreResponse setAccelerateEndpoint(String accelerateEndpoint) {
        this.accelerateEndpoint = accelerateEndpoint;
        return this;
    }
    public String getAccelerateEndpoint() {
        return this.accelerateEndpoint;
    }

    public AddStoreResponse setBasePath(String basePath) {
        this.basePath = basePath;
        return this;
    }
    public String getBasePath() {
        return this.basePath;
    }

    public AddStoreResponse setBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }
    public String getBucket() {
        return this.bucket;
    }

    public AddStoreResponse setCdnEndpoint(String cdnEndpoint) {
        this.cdnEndpoint = cdnEndpoint;
        return this;
    }
    public String getCdnEndpoint() {
        return this.cdnEndpoint;
    }

    public AddStoreResponse setCustomizedAccelerateEndpoint(String customizedAccelerateEndpoint) {
        this.customizedAccelerateEndpoint = customizedAccelerateEndpoint;
        return this;
    }
    public String getCustomizedAccelerateEndpoint() {
        return this.customizedAccelerateEndpoint;
    }

    public AddStoreResponse setCustomizedCdnEndpoint(String customizedCdnEndpoint) {
        this.customizedCdnEndpoint = customizedCdnEndpoint;
        return this;
    }
    public String getCustomizedCdnEndpoint() {
        return this.customizedCdnEndpoint;
    }

    public AddStoreResponse setCustomizedEndpoint(String customizedEndpoint) {
        this.customizedEndpoint = customizedEndpoint;
        return this;
    }
    public String getCustomizedEndpoint() {
        return this.customizedEndpoint;
    }

    public AddStoreResponse setCustomizedInternalEndpoint(String customizedInternalEndpoint) {
        this.customizedInternalEndpoint = customizedInternalEndpoint;
        return this;
    }
    public String getCustomizedInternalEndpoint() {
        return this.customizedInternalEndpoint;
    }

    public AddStoreResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public AddStoreResponse setEndpoint(String endpoint) {
        this.endpoint = endpoint;
        return this;
    }
    public String getEndpoint() {
        return this.endpoint;
    }

    public AddStoreResponse setInternalEndpoint(String internalEndpoint) {
        this.internalEndpoint = internalEndpoint;
        return this;
    }
    public String getInternalEndpoint() {
        return this.internalEndpoint;
    }

    public AddStoreResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public AddStoreResponse setOwnership(String ownership) {
        this.ownership = ownership;
        return this;
    }
    public String getOwnership() {
        return this.ownership;
    }

    public AddStoreResponse setPolicy(String policy) {
        this.policy = policy;
        return this;
    }
    public String getPolicy() {
        return this.policy;
    }

    public AddStoreResponse setRoleArn(String roleArn) {
        this.roleArn = roleArn;
        return this;
    }
    public String getRoleArn() {
        return this.roleArn;
    }

    public AddStoreResponse setStoreId(String storeId) {
        this.storeId = storeId;
        return this;
    }
    public String getStoreId() {
        return this.storeId;
    }

    public AddStoreResponse setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
