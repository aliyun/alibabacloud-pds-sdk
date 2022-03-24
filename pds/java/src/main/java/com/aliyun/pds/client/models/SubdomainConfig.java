// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SubdomainConfig extends TeaModel {
    @NameInMap("enable_root_domain_create_resource")
    public Boolean enableRootDomainCreateResource;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("independent_store_count_quota")
    public Long independentStoreCountQuota;

    @NameInMap("subdomain_count_quota")
    public Long subdomainCountQuota;

    @NameInMap("version")
    public String version;

    public static SubdomainConfig build(java.util.Map<String, ?> map) throws Exception {
        SubdomainConfig self = new SubdomainConfig();
        return TeaModel.build(map, self);
    }

    public SubdomainConfig setEnableRootDomainCreateResource(Boolean enableRootDomainCreateResource) {
        this.enableRootDomainCreateResource = enableRootDomainCreateResource;
        return this;
    }
    public Boolean getEnableRootDomainCreateResource() {
        return this.enableRootDomainCreateResource;
    }

    public SubdomainConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public SubdomainConfig setIndependentStoreCountQuota(Long independentStoreCountQuota) {
        this.independentStoreCountQuota = independentStoreCountQuota;
        return this;
    }
    public Long getIndependentStoreCountQuota() {
        return this.independentStoreCountQuota;
    }

    public SubdomainConfig setSubdomainCountQuota(Long subdomainCountQuota) {
        this.subdomainCountQuota = subdomainCountQuota;
        return this;
    }
    public Long getSubdomainCountQuota() {
        return this.subdomainCountQuota;
    }

    public SubdomainConfig setVersion(String version) {
        this.version = version;
        return this;
    }
    public String getVersion() {
        return this.version;
    }

}
