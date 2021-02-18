<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class StoreItemResponse extends Model
{
    /**
     * @description 全球加速地址
     *
     * @example https://oss-cn-shenzhen.aliyuncs.com/
     *
     * @var string
     */
    public $accelerateEndpoint;

    /**
     * @description 存储公共前缀
     *
     * @example pds-data
     *
     * @var string
     */
    public $basePath;

    /**
     * @description bucket名称
     *
     * @example data-sz-bucket
     *
     * @var string
     */
    public $bucket;

    /**
     * @description 内容分发地址
     *
     * @example https://oss-cn-shenzhen.aliyuncs.com/
     *
     * @var string
     */
    public $cdnEndpoint;

    /**
     * @description 自定义全球加速地址
     *
     * @example https://oss-cn-shenzhen.aliyuncs.com/
     *
     * @var string
     */
    public $customizedAccelerateEndpoint;

    /**
     * @description 自定义内容分发地址
     *
     * @example https://oss-cn-shenzhen.aliyuncs.com/
     *
     * @var string
     */
    public $customizedCdnEndpoint;

    /**
     * @description 自定义Public访问地址
     *
     * @example https://{regionid}-data.mydomain.com/
     *
     * @var string
     */
    public $customizedEndpoint;

    /**
     * @description 自定义vpc访问地址
     *
     * @example https://{regionid}-data-vpc.mydomain.com/
     *
     * @var string
     */
    public $customizedInternalEndpoint;

    /**
     * @var string
     */
    public $domainId;

    /**
     * @description Public访问地址
     *
     * @example https://{domainid}.{regionid}.data.aliyunpds.com/
     *
     * @var string
     */
    public $endpoint;

    /**
     * @description vpc访问地址
     *
     * @example https://{domainid}.{regionid}.data-vpc.aliyunpds.com/
     *
     * @var string
     */
    public $internalEndpoint;

    /**
     * @description 地点
     *
     * @example cn-hangzhou
     *
     * @var string
     */
    public $location;

    /**
     * @description 存储归属，system表示系统提供，custom表示使用自己的存储
     *
     * @example system
     *
     * @var string
     */
    public $ownership;

    /**
     * @description Policy授权,system类型store会将bucket权限授予当前云账号
     *
     * @var string
     */
    public $policy;

    /**
     * @description 访问Bucket的角色ARN
     *
     * @example acs:oss:*:*:*
     *
     * @var string
     */
    public $roleArn;

    /**
     * @description store ID
     *
     * @example 101
     *
     * @var string
     */
    public $storeId;

    /**
     * @description 存储类型，当前只支持oss
     *
     * @example oss
     *
     * @var string
     */
    public $type;
    protected $_name = [
        'accelerateEndpoint'           => 'accelerate_endpoint',
        'basePath'                     => 'base_path',
        'bucket'                       => 'bucket',
        'cdnEndpoint'                  => 'cdn_endpoint',
        'customizedAccelerateEndpoint' => 'customized_accelerate_endpoint',
        'customizedCdnEndpoint'        => 'customized_cdn_endpoint',
        'customizedEndpoint'           => 'customized_endpoint',
        'customizedInternalEndpoint'   => 'customized_internal_endpoint',
        'domainId'                     => 'domain_id',
        'endpoint'                     => 'endpoint',
        'internalEndpoint'             => 'internal_endpoint',
        'location'                     => 'location',
        'ownership'                    => 'ownership',
        'policy'                       => 'policy',
        'roleArn'                      => 'role_arn',
        'storeId'                      => 'store_id',
        'type'                         => 'type',
    ];

    public function validate()
    {
        Model::validateRequired('bucket', $this->bucket, true);
        Model::validateRequired('endpoint', $this->endpoint, true);
        Model::validateRequired('ownership', $this->ownership, true);
        Model::validateRequired('policy', $this->policy, true);
        Model::validateRequired('storeId', $this->storeId, true);
        Model::validateRequired('type', $this->type, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->accelerateEndpoint) {
            $res['accelerate_endpoint'] = $this->accelerateEndpoint;
        }
        if (null !== $this->basePath) {
            $res['base_path'] = $this->basePath;
        }
        if (null !== $this->bucket) {
            $res['bucket'] = $this->bucket;
        }
        if (null !== $this->cdnEndpoint) {
            $res['cdn_endpoint'] = $this->cdnEndpoint;
        }
        if (null !== $this->customizedAccelerateEndpoint) {
            $res['customized_accelerate_endpoint'] = $this->customizedAccelerateEndpoint;
        }
        if (null !== $this->customizedCdnEndpoint) {
            $res['customized_cdn_endpoint'] = $this->customizedCdnEndpoint;
        }
        if (null !== $this->customizedEndpoint) {
            $res['customized_endpoint'] = $this->customizedEndpoint;
        }
        if (null !== $this->customizedInternalEndpoint) {
            $res['customized_internal_endpoint'] = $this->customizedInternalEndpoint;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->endpoint) {
            $res['endpoint'] = $this->endpoint;
        }
        if (null !== $this->internalEndpoint) {
            $res['internal_endpoint'] = $this->internalEndpoint;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->ownership) {
            $res['ownership'] = $this->ownership;
        }
        if (null !== $this->policy) {
            $res['policy'] = $this->policy;
        }
        if (null !== $this->roleArn) {
            $res['role_arn'] = $this->roleArn;
        }
        if (null !== $this->storeId) {
            $res['store_id'] = $this->storeId;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return StoreItemResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['accelerate_endpoint'])) {
            $model->accelerateEndpoint = $map['accelerate_endpoint'];
        }
        if (isset($map['base_path'])) {
            $model->basePath = $map['base_path'];
        }
        if (isset($map['bucket'])) {
            $model->bucket = $map['bucket'];
        }
        if (isset($map['cdn_endpoint'])) {
            $model->cdnEndpoint = $map['cdn_endpoint'];
        }
        if (isset($map['customized_accelerate_endpoint'])) {
            $model->customizedAccelerateEndpoint = $map['customized_accelerate_endpoint'];
        }
        if (isset($map['customized_cdn_endpoint'])) {
            $model->customizedCdnEndpoint = $map['customized_cdn_endpoint'];
        }
        if (isset($map['customized_endpoint'])) {
            $model->customizedEndpoint = $map['customized_endpoint'];
        }
        if (isset($map['customized_internal_endpoint'])) {
            $model->customizedInternalEndpoint = $map['customized_internal_endpoint'];
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }
        if (isset($map['endpoint'])) {
            $model->endpoint = $map['endpoint'];
        }
        if (isset($map['internal_endpoint'])) {
            $model->internalEndpoint = $map['internal_endpoint'];
        }
        if (isset($map['location'])) {
            $model->location = $map['location'];
        }
        if (isset($map['ownership'])) {
            $model->ownership = $map['ownership'];
        }
        if (isset($map['policy'])) {
            $model->policy = $map['policy'];
        }
        if (isset($map['role_arn'])) {
            $model->roleArn = $map['role_arn'];
        }
        if (isset($map['store_id'])) {
            $model->storeId = $map['store_id'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }

        return $model;
    }
}
