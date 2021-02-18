<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\AppAccessStrategy;

/**
 * create domain request
 */
class CreateDomainRequest extends Model {
    protected $_name = [
        'authConfig' => 'auth_config',
        'authDingdingAppId' => 'auth_dingding_app_id',
        'authDingdingAppSecret' => 'auth_dingding_app_secret',
        'authDingdingEnable' => 'auth_dingding_enable',
        'authEndpointEnable' => 'auth_endpoint_enable',
        'authRamAppId' => 'auth_ram_app_id',
        'authRamAppSecret' => 'auth_ram_app_secret',
        'authRamEnable' => 'auth_ram_enable',
        'dataHashName' => 'data_hash_name',
        'description' => 'description',
        'domainName' => 'domain_name',
        'eventFilenameMatches' => 'event_filename_matches',
        'eventMnsEndpoint' => 'event_mns_endpoint',
        'eventMnsTopic' => 'event_mns_topic',
        'eventNames' => 'event_names',
        'eventRoleArn' => 'event_role_arn',
        'initDriveEnable' => 'init_drive_enable',
        'initDriveSize' => 'init_drive_size',
        'mode' => 'mode',
        'pathType' => 'path_type',
        'publishedAppAccessStrategy' => 'published_app_access_strategy',
        'sharable' => 'sharable',
        'storeLevel' => 'store_level',
        'storeRegionList' => 'store_region_list',
    ];
    public function validate() {
        Model::validateRequired('domainName', $this->domainName, true);
        Model::validateRequired('mode', $this->mode, true);
        Model::validateRequired('storeRegionList', $this->storeRegionList, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->authConfig) {
            $res['auth_config'] = $this->authConfig;
        }
        if (null !== $this->authDingdingAppId) {
            $res['auth_dingding_app_id'] = $this->authDingdingAppId;
        }
        if (null !== $this->authDingdingAppSecret) {
            $res['auth_dingding_app_secret'] = $this->authDingdingAppSecret;
        }
        if (null !== $this->authDingdingEnable) {
            $res['auth_dingding_enable'] = $this->authDingdingEnable;
        }
        if (null !== $this->authEndpointEnable) {
            $res['auth_endpoint_enable'] = $this->authEndpointEnable;
        }
        if (null !== $this->authRamAppId) {
            $res['auth_ram_app_id'] = $this->authRamAppId;
        }
        if (null !== $this->authRamAppSecret) {
            $res['auth_ram_app_secret'] = $this->authRamAppSecret;
        }
        if (null !== $this->authRamEnable) {
            $res['auth_ram_enable'] = $this->authRamEnable;
        }
        if (null !== $this->dataHashName) {
            $res['data_hash_name'] = $this->dataHashName;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->domainName) {
            $res['domain_name'] = $this->domainName;
        }
        if (null !== $this->eventFilenameMatches) {
            $res['event_filename_matches'] = $this->eventFilenameMatches;
        }
        if (null !== $this->eventMnsEndpoint) {
            $res['event_mns_endpoint'] = $this->eventMnsEndpoint;
        }
        if (null !== $this->eventMnsTopic) {
            $res['event_mns_topic'] = $this->eventMnsTopic;
        }
        if (null !== $this->eventNames) {
            $res['event_names'] = $this->eventNames;
        }
        if (null !== $this->eventRoleArn) {
            $res['event_role_arn'] = $this->eventRoleArn;
        }
        if (null !== $this->initDriveEnable) {
            $res['init_drive_enable'] = $this->initDriveEnable;
        }
        if (null !== $this->initDriveSize) {
            $res['init_drive_size'] = $this->initDriveSize;
        }
        if (null !== $this->mode) {
            $res['mode'] = $this->mode;
        }
        if (null !== $this->pathType) {
            $res['path_type'] = $this->pathType;
        }
        if (null !== $this->publishedAppAccessStrategy) {
            $res['published_app_access_strategy'] = null !== $this->publishedAppAccessStrategy ? $this->publishedAppAccessStrategy->toMap() : null;
        }
        if (null !== $this->sharable) {
            $res['sharable'] = $this->sharable;
        }
        if (null !== $this->storeLevel) {
            $res['store_level'] = $this->storeLevel;
        }
        if (null !== $this->storeRegionList) {
            $res['store_region_list'] = $this->storeRegionList;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return CreateDomainRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['auth_config'])){
            $model->authConfig = $map['auth_config'];
        }
        if(isset($map['auth_dingding_app_id'])){
            $model->authDingdingAppId = $map['auth_dingding_app_id'];
        }
        if(isset($map['auth_dingding_app_secret'])){
            $model->authDingdingAppSecret = $map['auth_dingding_app_secret'];
        }
        if(isset($map['auth_dingding_enable'])){
            $model->authDingdingEnable = $map['auth_dingding_enable'];
        }
        if(isset($map['auth_endpoint_enable'])){
            $model->authEndpointEnable = $map['auth_endpoint_enable'];
        }
        if(isset($map['auth_ram_app_id'])){
            $model->authRamAppId = $map['auth_ram_app_id'];
        }
        if(isset($map['auth_ram_app_secret'])){
            $model->authRamAppSecret = $map['auth_ram_app_secret'];
        }
        if(isset($map['auth_ram_enable'])){
            $model->authRamEnable = $map['auth_ram_enable'];
        }
        if(isset($map['data_hash_name'])){
            $model->dataHashName = $map['data_hash_name'];
        }
        if(isset($map['description'])){
            $model->description = $map['description'];
        }
        if(isset($map['domain_name'])){
            $model->domainName = $map['domain_name'];
        }
        if(isset($map['event_filename_matches'])){
            $model->eventFilenameMatches = $map['event_filename_matches'];
        }
        if(isset($map['event_mns_endpoint'])){
            $model->eventMnsEndpoint = $map['event_mns_endpoint'];
        }
        if(isset($map['event_mns_topic'])){
            $model->eventMnsTopic = $map['event_mns_topic'];
        }
        if(isset($map['event_names'])){
            if(!empty($map['event_names'])){
                $model->eventNames = $map['event_names'];
            }
        }
        if(isset($map['event_role_arn'])){
            $model->eventRoleArn = $map['event_role_arn'];
        }
        if(isset($map['init_drive_enable'])){
            $model->initDriveEnable = $map['init_drive_enable'];
        }
        if(isset($map['init_drive_size'])){
            $model->initDriveSize = $map['init_drive_size'];
        }
        if(isset($map['mode'])){
            $model->mode = $map['mode'];
        }
        if(isset($map['path_type'])){
            $model->pathType = $map['path_type'];
        }
        if(isset($map['published_app_access_strategy'])){
            $model->publishedAppAccessStrategy = AppAccessStrategy::fromMap($map['published_app_access_strategy']);
        }
        if(isset($map['sharable'])){
            $model->sharable = $map['sharable'];
        }
        if(isset($map['store_level'])){
            $model->storeLevel = $map['store_level'];
        }
        if(isset($map['store_region_list'])){
            if(!empty($map['store_region_list'])){
                $model->storeRegionList = $map['store_region_list'];
            }
        }
        return $model;
    }
    /**
     * @description 登录相关信息
     * @example {}
     * @var mixed[]
     */
    public $authConfig;

    /**
     * @description 钉钉 App Id
     * @example abc
     * @var string
     */
    public $authDingdingAppId;

    /**
     * @description 钉钉 App Secret
     * @example abc
     * @var string
     */
    public $authDingdingAppSecret;

    /**
     * @description 启用钉钉认证
     * @example true
     * @var bool
     */
    public $authDingdingEnable;

    /**
     * @var bool
     */
    public $authEndpointEnable;

    /**
     * @description RAM App Id
     * @example abc
     * @var string
     */
    public $authRamAppId;

    /**
     * @description RAM App Secret
     * @example abc
     * @var string
     */
    public $authRamAppSecret;

    /**
     * @description 启用 RAM 认证
     * @example true
     * @var bool
     */
    public $authRamEnable;

    /**
     * @description 数据 Hash 算法
     * @example sha1
     * @var string
     */
    public $dataHashName;

    /**
     * @description Domain 描述
     * @example my test domain
     * @var string
     */
    public $description;

    /**
     * @description Domain 名称
     * @example test_domain
     * @var string
     */
    public $domainName;

    /**
     * @description 事件通知 MNS 匹配文件名
     * @example abc
     * @var string
     */
    public $eventFilenameMatches;

    /**
     * @description 事件通知 MNS Endpoint
     * @example http://abc.mns.cn-shenzhen.aliyuncs.com
     * @var string
     */
    public $eventMnsEndpoint;

    /**
     * @description 事件通知 MNS Topic
     * @example abc
     * @var string
     */
    public $eventMnsTopic;

    /**
     * @description 事件名列表
     * @example abc
     * @var string[]
     */
    public $eventNames;

    /**
     * @description 事件通知 Role Arn
     * @var string
     */
    public $eventRoleArn;

    /**
     * @description 开启自动初始化 Drive
     * @example true
     * @var bool
     */
    public $initDriveEnable;

    /**
     * @description 自动初始化 Drive 大小
     * @example 1024
     * @var int
     */
    public $initDriveSize;

    /**
     * @description Domain 类型
     * @example StandardMode
     * @var string
     */
    public $mode;

    /**
     * @description Domain 类型
     * @example CCPPath
     * @var string
     */
    public $pathType;

    /**
     * @var AppAccessStrategy
     */
    public $publishedAppAccessStrategy;

    /**
     * @description 开启分享
     * @example true
     * @var bool
     */
    public $sharable;

    /**
     * @description 存储级别
     * @example Standard
     * @var string
     */
    public $storeLevel;

    /**
     * @description 存储 Region 列表
     * @example cn-hangzhou
     * @var string[]
     */
    public $storeRegionList;

}
