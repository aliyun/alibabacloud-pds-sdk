<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * create share request.
 */
class CreateShareRequest extends Model
{
    public $headers;

    /**
     * @description description
     *
     * @example share description
     *
     * @var string
     */
    public $description;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description expiration
     *
     * @example 2006-01-02T15:04:05.999Z
     *
     * @var string
     */
    public $expiration;

    /**
     * @description owner
     *
     * @example abc
     *
     * @var string
     */
    public $owner;

    /**
     * @description owner_type
     *
     * @var string
     */
    public $ownerType;

    /**
     * @description permissions
     *
     * @example
     *
     * @var string[]
     */
    public $permissions;

    /**
     * @description share_file_id
     *
     * @var string
     */
    public $shareFileId;

    /**
     * @description share_file_path
     *
     * @var string
     */
    public $shareFilePath;

    /**
     * @description share_name
     *
     * @example share
     *
     * @var string
     */
    public $shareName;

    /**
     * @description share create policy
     *
     * share_policy
     * @var SharePermissionPolicy[]
     */
    public $sharePolicy;

    /**
     * @description status
     *
     * @example enabled
     *
     * @var string
     */
    public $status;
    protected $_name = [
        'description'   => 'description',
        'driveId'       => 'drive_id',
        'expiration'    => 'expiration',
        'owner'         => 'owner',
        'ownerType'     => 'owner_type',
        'permissions'   => 'permissions',
        'shareFileId'   => 'share_file_id',
        'shareFilePath' => 'share_file_path',
        'shareName'     => 'share_name',
        'sharePolicy'   => 'share_policy',
        'status'        => 'status',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('owner', $this->owner, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
    }

    public function toMap()
    {
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
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->owner) {
            $res['owner'] = $this->owner;
        }
        if (null !== $this->ownerType) {
            $res['owner_type'] = $this->ownerType;
        }
        if (null !== $this->permissions) {
            $res['permissions'] = $this->permissions;
        }
        if (null !== $this->shareFileId) {
            $res['share_file_id'] = $this->shareFileId;
        }
        if (null !== $this->shareFilePath) {
            $res['share_file_path'] = $this->shareFilePath;
        }
        if (null !== $this->shareName) {
            $res['share_name'] = $this->shareName;
        }
        if (null !== $this->sharePolicy) {
            $res['share_policy'] = [];
            if (null !== $this->sharePolicy && \is_array($this->sharePolicy)) {
                $n = 0;
                foreach ($this->sharePolicy as $item) {
                    $res['share_policy'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->status) {
            $res['status'] = $this->status;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateShareRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['expiration'])) {
            $model->expiration = $map['expiration'];
        }
        if (isset($map['owner'])) {
            $model->owner = $map['owner'];
        }
        if (isset($map['owner_type'])) {
            $model->ownerType = $map['owner_type'];
        }
        if (isset($map['permissions'])) {
            if (!empty($map['permissions'])) {
                $model->permissions = $map['permissions'];
            }
        }
        if (isset($map['share_file_id'])) {
            $model->shareFileId = $map['share_file_id'];
        }
        if (isset($map['share_file_path'])) {
            $model->shareFilePath = $map['share_file_path'];
        }
        if (isset($map['share_name'])) {
            $model->shareName = $map['share_name'];
        }
        if (isset($map['share_policy'])) {
            if (!empty($map['share_policy'])) {
                $model->sharePolicy = [];
                $n                  = 0;
                foreach ($map['share_policy'] as $item) {
                    $model->sharePolicy[$n++] = null !== $item ? SharePermissionPolicy::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['status'])) {
            $model->status = $map['status'];
        }

        return $model;
    }
}
