<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Update drive request
 */
class UpdateDriveRequest extends Model {
    protected $_name = [
        'description' => 'description',
        'driveId' => 'drive_id',
        'driveName' => 'drive_name',
        'encryptDataAccess' => 'encrypt_data_access',
        'encryptMode' => 'encrypt_mode',
        'status' => 'status',
        'totalSize' => 'total_size',
    ];
    protected $_default = [
        'encryptDataAccess' => 'false',
        'status' => 'enabled',
        'totalSize' => 0,
    ];
    public function validate() {
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateMaxLength('driveName', $this->driveName, 1024);
        Model::validateRequired('driveId', $this->driveId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->driveName) {
            $res['drive_name'] = $this->driveName;
        }
        if (null !== $this->encryptDataAccess) {
            $res['encrypt_data_access'] = $this->encryptDataAccess;
        }
        if (null !== $this->encryptMode) {
            $res['encrypt_mode'] = $this->encryptMode;
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }
        if (null !== $this->totalSize) {
            $res['total_size'] = $this->totalSize;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return UpdateDriveRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['description'])){
            $model->description = $map['description'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['drive_name'])){
            $model->driveName = $map['drive_name'];
        }
        if(isset($map['encrypt_data_access'])){
            $model->encryptDataAccess = $map['encrypt_data_access'];
        }
        if(isset($map['encrypt_mode'])){
            $model->encryptMode = $map['encrypt_mode'];
        }
        if(isset($map['status'])){
            $model->status = $map['status'];
        }
        if(isset($map['total_size'])){
            $model->totalSize = $map['total_size'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description 描述信息
     * @example ccp team drive
     * @var string
     */
    public $description;

    /**
     * @description Drive ID
     * @example 123
     * @var string
     */
    public $driveId;

    /**
     * @description Drive 名称
     * @example ccpdrive
     * @var string
     */
    public $driveName;

    /**
     * @description 授权访问加密数据
     * @example true
     * @var bool
     */
    public $encryptDataAccess;

    /**
     * @description 加密模式
     * @example server
     * @var string
     */
    public $encryptMode;

    /**
     * @description 状态
     * @example enabled
     * @var string
     */
    public $status;

    /**
     * @description 总大小,单位Byte [如果设置 -1 代表不限制]
     * @example 1024
     * @var int
     */
    public $totalSize;

}
