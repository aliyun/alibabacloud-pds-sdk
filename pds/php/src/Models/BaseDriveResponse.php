<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Base drive response.
 */
class BaseDriveResponse extends Model
{
    /**
     * @description Drive 创建者
     *
     * @example ccp
     *
     * @var string
     */
    public $creator;

    /**
     * @description Drive 备注信息
     *
     * @example ccp team drive
     *
     * @var string
     */
    public $description;

    /**
     * @description Domain ID
     *
     * @example hz999
     *
     * @var string
     */
    public $domainId;

    /**
     * @description Drive ID
     *
     * @example 123
     *
     * @var string
     */
    public $driveId;

    /**
     * @description Drive 名称
     *
     * @example ccpdrive
     *
     * @var string
     */
    public $driveName;

    /**
     * @description Drive 类型
     *
     * @example normal
     *
     * @var string
     */
    public $driveType;

    /**
     * @var bool
     */
    public $encryptDataAccess;

    /**
     * @var string
     */
    public $encryptMode;

    /**
     * @description Drive 所有者
     *
     * @example ccp
     *
     * @var string
     */
    public $owner;

    /**
     * @description Drive 所有者类型
     *
     * @example user
     *
     * @var string
     */
    public $ownerType;

    /**
     * @description Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
     *
     * @example /a/b/e/
     *
     * @var string
     */
    public $relativePath;

    /**
     * @description Drive 状态
     *
     * @example enabled
     *
     * @var string
     */
    public $status;

    /**
     * @description 存储 ID, domain的PathType为OSSPath时返回
     *
     * @example 123
     *
     * @var string
     */
    public $storeId;

    /**
     * @description Drive 空间总量
     *
     * @example 102400
     *
     * @var int
     */
    public $totalSize;

    /**
     * @description Drive 空间已使用量
     *
     * @example 1024
     *
     * @var int
     */
    public $usedSize;
    protected $_name = [
        'creator'           => 'creator',
        'description'       => 'description',
        'domainId'          => 'domain_id',
        'driveId'           => 'drive_id',
        'driveName'         => 'drive_name',
        'driveType'         => 'drive_type',
        'encryptDataAccess' => 'encrypt_data_access',
        'encryptMode'       => 'encrypt_mode',
        'owner'             => 'owner',
        'ownerType'         => 'owner_type',
        'relativePath'      => 'relative_path',
        'status'            => 'status',
        'storeId'           => 'store_id',
        'totalSize'         => 'total_size',
        'usedSize'          => 'used_size',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->creator) {
            $res['creator'] = $this->creator;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->driveName) {
            $res['drive_name'] = $this->driveName;
        }
        if (null !== $this->driveType) {
            $res['drive_type'] = $this->driveType;
        }
        if (null !== $this->encryptDataAccess) {
            $res['encrypt_data_access'] = $this->encryptDataAccess;
        }
        if (null !== $this->encryptMode) {
            $res['encrypt_mode'] = $this->encryptMode;
        }
        if (null !== $this->owner) {
            $res['owner'] = $this->owner;
        }
        if (null !== $this->ownerType) {
            $res['owner_type'] = $this->ownerType;
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
        if (null !== $this->usedSize) {
            $res['used_size'] = $this->usedSize;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseDriveResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['creator'])) {
            $model->creator = $map['creator'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['drive_name'])) {
            $model->driveName = $map['drive_name'];
        }
        if (isset($map['drive_type'])) {
            $model->driveType = $map['drive_type'];
        }
        if (isset($map['encrypt_data_access'])) {
            $model->encryptDataAccess = $map['encrypt_data_access'];
        }
        if (isset($map['encrypt_mode'])) {
            $model->encryptMode = $map['encrypt_mode'];
        }
        if (isset($map['owner'])) {
            $model->owner = $map['owner'];
        }
        if (isset($map['owner_type'])) {
            $model->ownerType = $map['owner_type'];
        }
        if (isset($map['relative_path'])) {
            $model->relativePath = $map['relative_path'];
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }
        if (isset($map['store_id'])) {
            $model->storeId = $map['store_id'];
        }
        if (isset($map['total_size'])) {
            $model->totalSize = $map['total_size'];
        }
        if (isset($map['used_size'])) {
            $model->usedSize = $map['used_size'];
        }

        return $model;
    }
}
