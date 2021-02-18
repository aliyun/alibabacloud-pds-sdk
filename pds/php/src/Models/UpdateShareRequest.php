<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\SharePermissionPolicy;

/**
 * update share request
 */
class UpdateShareRequest extends Model {
    protected $_name = [
        'description' => 'description',
        'expiration' => 'expiration',
        'permissions' => 'permissions',
        'shareId' => 'share_id',
        'shareName' => 'share_name',
        'sharePolicy' => 'share_policy',
        'status' => 'status',
    ];
    public function validate() {
        Model::validateMaxLength('description', $this->description, 1024);
        Model::validateRequired('shareId', $this->shareId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->permissions) {
            $res['permissions'] = $this->permissions;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->shareName) {
            $res['share_name'] = $this->shareName;
        }
        if (null !== $this->sharePolicy) {
            $res['share_policy'] = [];
            if(null !== $this->sharePolicy && is_array($this->sharePolicy)){
                $n = 0;
                foreach($this->sharePolicy as $item){
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
     * @return UpdateShareRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['description'])){
            $model->description = $map['description'];
        }
        if(isset($map['expiration'])){
            $model->expiration = $map['expiration'];
        }
        if(isset($map['permissions'])){
            if(!empty($map['permissions'])){
                $model->permissions = $map['permissions'];
            }
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['share_name'])){
            $model->shareName = $map['share_name'];
        }
        if(isset($map['share_policy'])){
            if(!empty($map['share_policy'])){
                $model->sharePolicy = [];
                $n = 0;
                foreach($map['share_policy'] as $item) {
                    $model->sharePolicy[$n++] = null !== $item ? SharePermissionPolicy::fromMap($item) : $item;
                }
            }
        }
        if(isset($map['status'])){
            $model->status = $map['status'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description description
     * @example share description
     * @var string
     */
    public $description;

    /**
     * @description expiration
     * @example 2006-01-02T15:04:05.999Z
     * @var string
     */
    public $expiration;

    /**
     * @description permissions
     * @example 
     * @var string[]
     */
    public $permissions;

    /**
     * @description share_id
     * @example 3d336314-63c8-4d96-bce0-17aefb6833b6
     * @var string
     */
    public $shareId;

    /**
     * @description share_name
     * @example new_share_name
     * @var string
     */
    public $shareName;

    /**
     * @description share_policy
     * @var SharePermissionPolicy[]
     */
    public $sharePolicy;

    /**
     * @description status
     * @example enabled
     * @var string
     */
    public $status;

}
