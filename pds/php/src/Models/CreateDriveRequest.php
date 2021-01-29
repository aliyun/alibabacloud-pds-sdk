<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * create drive request
 */
class CreateDriveRequest extends Model {
    protected $_name = [
        'default' => 'default',
        'description' => 'description',
        'driveName' => 'drive_name',
        'driveType' => 'drive_type',
        'encryptMode' => 'encrypt_mode',
        'location' => 'location',
        'owner' => 'owner',
        'relativePath' => 'relative_path',
        'status' => 'status',
        'storeId' => 'store_id',
        'totalSize' => 'total_size',
    ];
    protected $_default = [
        'default' => 'false',
        'driveType' => 'normal',
        'status' => 'enabled',
        'totalSize' => -1,
    ];
    public function validate() {
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateMaxLength('driveName', $this->driveName, 1024);
        Model::validateRequired('driveName', $this->driveName, true);
        Model::validateRequired('owner', $this->owner, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->default) {
            $res['default'] = $this->default;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->driveName) {
            $res['drive_name'] = $this->driveName;
        }
        if (null !== $this->driveType) {
            $res['drive_type'] = $this->driveType;
        }
        if (null !== $this->encryptMode) {
            $res['encrypt_mode'] = $this->encryptMode;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->owner) {
            $res['owner'] = $this->owner;
        }
        if (null !== $this->relativePath) {
            $res['relative_path'] = $this->relativePath;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->storeId) {
            $res['store_id'] = $this->storeId;
        }
        if (null !== $this->totalSize) {
            $res['total_size'] = $this->totalSize;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return CreateDriveRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['default'])){
            $model->default = $map['default'];
        }
        if(isset($map['description'])){
            $model->description = $map['description'];
        }
        if(isset($map['drive_name'])){
            $model->driveName = $map['drive_name'];
        }
        if(isset($map['drive_type'])){
            $model->driveType = $map['drive_type'];
        }
        if(isset($map['encrypt_mode'])){
            $model->encryptMode = $map['encrypt_mode'];
        }
        if(isset($map['location'])){
            $model->location = $map['location'];
        }
        if(isset($map['owner'])){
            $model->owner = $map['owner'];
        }
        if(isset($map['relative_path'])){
            $model->relativePath = $map['relative_path'];
        }
        if(isset($map['status'])){
            $model->status = $map['status'];
        }
        if(isset($map['store_id'])){
            $model->storeId = $map['store_id'];
        }
        if(isset($map['total_size'])){
            $model->totalSize = $map['total_size'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description 是否默认drive, 只允许设置一个默认drive
     * @example true
     * @var bool
     */
    public $default;

    /**
     * @description 描述信息
     * @example ccp team drive
     * @var string
     */
    public $description;

    /**
     * @description Drive 名称
     * @example ccpdrive
     * @var string
     */
    public $driveName;

    /**
     * @description Drive类型
     * @example normal
     * @var string
     */
    public $driveType;

    /**
     * @var string
     */
    public $encryptMode;

    /**
     * @description location
     * @example cn-hangzhou
     * @var string
     */
    public $location;

    /**
     * @description 所属者
     * @example ccp-001
     * @var string
     */
    public $owner;

    /**
     * @description domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
     * @example /d/e/f/
     * @var string
     */
    public $relativePath;

    /**
     * @description 状态
     * @example enabled
     * @var string
     */
    public $status;

    /**
     * @description StoreID , domain的PathType为OSSPath时必选
     * @example store_id
     * @var string
     */
    public $storeId;

    /**
     * @description 总大小,单位Byte [如果设置 -1 代表不限制]
     * @example 1024
     * @var int
     */
    public $totalSize;

}
